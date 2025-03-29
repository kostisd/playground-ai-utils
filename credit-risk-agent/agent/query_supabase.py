import os
import re
import traceback
from supabase import create_client, Client
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Connect
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def query_supabase(sql:str) -> str:
    """
    Handles simple SELECT queries for the 'credit_applications' table.
    Extracts basic SELECT filters and runs them using the Supabase SDK.
    """

    if not re.match(r"(?i)select .* from credit_applications", sql):
        return "Error: Only SELECT queries from the 'credit_applications' table are supported."
    
    try:
        original_sql = sql.strip().rstrip(";")
        sql = original_sql.lower()
        print(f"sql received: {original_sql}")
    
        # Get columns or *
        cols_match = re.search(r"select (.+?) from", sql)
        columns = cols_match.group(1).strip() if cols_match else "*"
        columns = "*" if columns == "*" else [col.strip() for col in columns.split(",")]

        # Extract basic WHERE clause
        filters_match = re.search(r"where (.+)", original_sql, re.IGNORECASE)
        filters = filters_match.group(1).strip() if filters_match else None
        
        if columns == "*":
            query = supabase.table("credit_applications").select("*")
        else:
            query = supabase.table("credit_applications").select(columns)

        if filters:
        # parse filter column
            if "!=" in filters or "=" in filters or "<>" in filters:
                operator = "!=" if "!=" in filters else "<>" if "<>" in filters else "="
                key, value = [part.strip() for part in filters.split(operator, 1)]
                value = value.strip("'\"")
                # add filter column to selected columns
                if key not in columns and columns != "*":
                    columns.append(key)
                query = query.eq(key, value) if operator == "=" else query.neq(key, value)

        print("parsed columns: ", columns)
        
        response = query.execute()
        data = response.data
        print("Supabase response:", data)

        if not data:
            return "Query succeeded, but returned no results."

        df = pd.DataFrame(data)
        return df.to_string(index=False)

    except Exception as e:
        print("Exception caught")
        traceback.print_exc()
        return f"Failed to run SELECT:\n{e}"
                
def query_supabase_edit(sql: str) -> str:
    """
    Runs raw SQL on Supabase using the sql_exec function
    Returns results as a stringified table
    """
    try:
        response = supabase.rpc("sql_exec", {"query": sql}).execute()
        return "Query executed successfully (no result returned)."
    except Exception as e:
        return f"Failed to run SQL:\n{e}"
