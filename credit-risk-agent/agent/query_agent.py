import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from tools import supabase_sql_tool
from prompts import query_prefix
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="langchain")

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

# Load tools
tools = [supabase_sql_tool]

# Create the agent
agent = initialize_agent(
    tools,
    llm,
    agent_kwargs={"prefix": query_prefix},
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

def main():
    print("Ask a question about the credit risk dataset (or type 'exit'):")
    while True:
        query = input(">")
        if query.lower() in {"exit", "quit"}:
            break
        response = agent.invoke(query)
        print(f"{response}\n")

if __name__ == "__main__":
    main()
