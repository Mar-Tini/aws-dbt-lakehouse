import pandas as pd  # type: ignore
import os
from sqlalchemy import create_engine, text  # type: ignore

# Load environment variables
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

# Use the DB_HOST from environment variable or default to "postgres" for Docker setup
DB_HOST = "postgres"
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "ecommerce")

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# CREATE SCHEMA IF NOT EXISTS analytics
with engine.connect() as conn:
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS analytics"))
    conn.commit()



df_sales = pd.read_csv(f"data/processed/data_clean.csv")

# Load the DataFrame into the "sales" table in the "analytics" schema
df_sales.to_sql("sales", engine, schema="analytics", if_exists="replace", index=False)


print("Data loaded successfully into schema analytics")