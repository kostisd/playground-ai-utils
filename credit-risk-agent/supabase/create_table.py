import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# SQL to create table
create_table_sql = """
CREATE TABLE IF NOT EXISTS credit_applications (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    age INTEGER,
    gender TEXT,
    education_level TEXT,
    marital_status TEXT,
    income FLOAT,
    credit_score FLOAT,
    load_amount FLOAT,
    loan_purpose TEXT,
    employment_status TEXT,
    years_at_current_job INTEGER,
    payment_history TEXT,
    debt_to_income_ratio FLOAT,
    assets_value FLOAT,
    number_of_dependents INTEGER,
    city TEXT,
    state TEXT,
    country TEXT,
    previous_defaults INTEGER,
    marital_status_change INTEGER,
    risk_rating TEXT
);
"""

# Call Supabase RPC to run SQL
try:
    response = supabase.rpc("sql_exec", {"query": create_table_sql}).execute()
    print("Table created or already exists.")
except Exception as e:
    print("Failed to create table:")
    print(e)

