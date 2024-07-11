
# reports/utils.py
import pandas as pd

def process_excel(file_path):
    df = pd.read_excel(file_path)
    # Normalize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    daily_total_sales = df.groupby('store_id')['total_sales'].sum().reset_index()
    top_selling_product = df.groupby('store_id').apply(lambda x: x.loc[x['quantity_sold'].idxmax()]).reset_index(drop=True)
    total_sales_by_product = df.groupby('product_id')['total_sales'].sum().reset_index()
    return daily_total_sales, top_selling_product, total_sales_by_product


