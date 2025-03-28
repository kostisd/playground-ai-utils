import os
from supabase import create_clinet, Client
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Connect
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def query_supabase(sql: str) -> str:
    """
    Runs raw SQL on Supabase using the sql_exec function
    Returns results as a stringified table
    """
    try:
        response = supabase.rpc("sql_exec", {"query": sql}).execute()
        return "Query executed successfully (no result returned)."
    except Exception as e:
        return f"Failed to run SQL:\n{e}"
