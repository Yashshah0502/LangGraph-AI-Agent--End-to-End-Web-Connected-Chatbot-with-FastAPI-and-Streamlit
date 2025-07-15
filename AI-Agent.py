import os
from dotenv import load_dotenv

load_dotenv()

GROO_API_KEY = os.getenv("GROO_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

openai_llm = ChatOpenAI(model="gpt-4o-mini")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROO_API_KEY)

search_tool = TavilySearch(max_results=2, api_key=TAVILY_API_KEY)

system_prompt = "Act as an AI chatbot who is smart and friendly"

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage


# Try without state_modifier first to see if that's the issue
agent = create_react_agent(
    model=groq_llm,
    tools=[search_tool])

query = "tell me about the latest news in AI"
response = agent.invoke({"messages": [("user", query)]})
messages = response.get("messages")
ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
print(ai_messages[-1])
# print(response)