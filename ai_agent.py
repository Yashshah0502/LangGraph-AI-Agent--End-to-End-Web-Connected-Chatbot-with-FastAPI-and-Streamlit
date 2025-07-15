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

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    # API key configuration
    if provider == "Groq":
        llm = ChatGroq(model=llm_id, api_key=GROO_API_KEY)  # Need to pass API key
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id, api_key=openai_api_key)  # Need to pass API key
    else:
        raise ValueError(f"Unsupported provider: {provider}")
    
    # Tools configuration - use TavilySearch instead of TavilySearchResults
    tools = [TavilySearch(max_results=2, api_key=TAVILY_API_KEY)] if allow_search else []
    
    # Create agent
    agent = create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )
    
    # Correct state format - query should be in a list with user role
    state = {"messages": [("user", query)]}
    
    # Invoke agent
    response = agent.invoke(state)
    messages = response.get("messages", [])
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    
    # Return the last AI message, or empty string if no AI messages
    return ai_messages[-1] if ai_messages else ""