from pathlib import Path
import pandas as pd


FILES = {
    "orders": "olist_orders_dataset.csv",
    "customers": "olist_customers_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "items": "olist_order_items_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "geo": "olist_geolocation_dataset.csv",
}


def load_data(data_dir):
    data_dir = Path(data_dir)
    return {
        name: pd.read_csv(data_dir / filename)
        for name, filename in FILES.items()
    }