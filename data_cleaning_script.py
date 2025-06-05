import pandas as pd
from datetime import datetime

df = pd.read_csv("shopify_reviews_raw.csv")

# Standardize timestamp
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

# Normalize text fields
df['Product Category'] = df['Product Category'].str.strip().str.title()
df['Product Name'] = df['Product Name'].str.strip().str.title()

# Filter out invalid reviews
df = df[df['Review Content'].str.len() > 10]
df = df[df['Rating'].between(1, 5, inclusive='both')]

# Handle missing ratings
df['Rating'] = df['Rating'].fillna(df['Rating'].mean())

# Save cleaned CSV
df.to_csv("shopify_reviews_cleaned.csv", index=False)
