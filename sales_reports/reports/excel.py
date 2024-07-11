
import pandas as pd
from reports.models import RawData, ProcessedData

def process_excel(file_path):
    df = pd.read_excel(file_path)
    
    # Save raw data
    for _, row in df.iterrows():
        RawData.objects.create(
            store_id=row['Store ID'],
            date=row['Date'],
            product_id=row['Product ID'],
            quantity_sold=row['Quantity Sold'],
            total_sales=row['Total Sales'],
        )

    # Calculate daily total sales for each store
    daily_sales = df.groupby(['Store ID', 'Date']).agg({'Total Sales': 'sum'}).reset_index()
    
    # Calculate top selling product for each store and date
    top_selling_product = df.groupby(['Store ID', 'Date', 'Product ID'])['Quantity Sold'].sum().reset_index()
    top_selling_product = top_selling_product.sort_values('Quantity Sold', ascending=False).drop_duplicates(['Store ID', 'Date'])
    top_selling_product = top_selling_product[['Store ID', 'Date', 'Product ID']].rename(columns={'Product ID': 'Top Selling Product'})

    # Merge daily sales with top selling product
    merged_data = pd.merge(daily_sales, top_selling_product, on=['Store ID', 'Date'], how='left')
    
    for _, row in merged_data.iterrows():
        ProcessedData.objects.create(
            store_id=row['Store ID'],
            date=row['Date'],
            total_sales=row['Total Sales'],
            top_selling_product=row['Top Selling Product'],
        )
    
    return merged_data
