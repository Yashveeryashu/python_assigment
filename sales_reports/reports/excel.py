import pandas as pd
from reports.models import RawData, ProcessedData

def process_excel(file_path):
    df = pd.read_excel(file_path)
    
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
    for _, row in daily_sales.iterrows():
        ProcessedData.objects.create(
            store_id=row['Store ID'],
            date=row['Date'],
            total_sales=row['Total Sales'],
            top_selling_product=row['Product ID'],  # Placeholder for top-selling product logic
        )
