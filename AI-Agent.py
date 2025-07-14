import os
from dotenv import load_dotenv

load_dotenv()

GROO_API_KEY = os.getenv("GROO_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

openai_llm = ChatOpenAI(model = "gpt-4o-min")
groq_llm = ChatGroq(model = "llama-3.3-70b-versatile")

search_tool = TavilySearchResults(max_results = 2)

