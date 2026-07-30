from annotated_types import DocInfo
from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
#from tavily import TavilyClient
from langchain import TavilySearch
#from langchain_ollama import ChatOllama


#tavily=TavilyClient()


#@tool
#def search(query: str) -> str:
 #   """
  #  Tool that searches over internet
  #  Args:
   #     query: The query to search for
  #  Returns:
   #     The search result
  #  """
   # print(f"Searching for {query}")
  #  #return "Tokyo weather is sunny"
 #   return tavily.search(query=query)
#
llm=ChatOpenAI()
#llm=ChatOllama(temperature=1, top_k=64, top_p=0.95, model="gemma3:270m")
tools=[TavilySearch()]
agent=create_agent(model=llm,tools=tools)


def main():
    print("Hello from chintan-langchain-course : react-agent-project !")
    result=agent.invoke({"messages":HumanMessage(content="Search for 3 job posting for a telecom BSS-OSS Solution architect in Germany and Switzerland on linked in and list their details?")})
    print(result)




if __name__ == "__main__":
    main()
