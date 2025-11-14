from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

@tool
def search(query: str) -> str:
    """
    This is a tool that searches the web for a given query.
    Arguments:
        query: The search query.
    Returns:
        The search results.
    """
    print(f"Searching for: {query}")
    return "Weather in Bengaluru is cloudy with a chance of rain."

#llm = ChatOpenAI(model="gpt-4", temperature=0)
#llm = ChatOllama(model="gemma3:270m", temperature=0.7)
llm = ChatOllama(model="qwen3:4b", temperature=0.7)
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello, Agent")
    agent_response = agent.invoke({"messages":HumanMessage(content="What's the weather like in Bengaluru?")})
    print(f"Agent Response: {agent_response}")


if __name__ == "__main__":
    main()