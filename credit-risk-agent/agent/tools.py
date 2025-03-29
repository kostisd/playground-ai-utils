from langchain.tools import Tool
from query_supabase import query_supabase

# Define LangChain tool
supabase_sql_tool = Tool(
    name="Supabase SQL Query Tool",
    func = query_supabase,
    description = (
        "Use this tool to run SQL queries on the credit risk dataset. "
        "Only use this tool when you need to answer questions that require data from the database. "
        "The table is called 'credit_applications'."
        )
    )
