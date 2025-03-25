import pandas as pd
import numpy as np
import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load .env
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
TABLE_NAME = os.getenv("SUPABASE_TABLE")

# Connect to Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Load and clean data
df = pd.read_csv("../data/financial_risk_assessment.csv")

# Convert columns to snake_case (so they match with the supabase table)

df.columns = (
	df.columns.str.strip()
	.str.lower()
	.str.replace(" ", "_")
	.str.replace("-", "_")
)

df = df.head(100)

# Optional: Preview columns and types
print("Uploading columns:", df.columns.tolist())
print(df.dtypes)

df = df.replace({np.nan: None})
records = df.to_dict(orient="records")

# Insert into Supabase
try:
    response = supabase.table(TABLE_NAME).insert(records).execute()
    print(f"Uploaded {len(records)} rows to Supabase.")
except Exception as e:
    print("Upload failed:")
    print(e)
