import streamlit as st
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="LangGraph AI Agent",
    page_icon=":robot_face:",
    layout="centered",
)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

st.title("LangGraph AI Agent")
st.write("This is a simple AI agent built with LangGraph and FastAPI. You can interact with it using the API endpoint provided below.")

# Configuration
system_prompt = st.text_area(
    "Define your AI Agent:", 
    height=100, 
    placeholder="Act as an AI chatbot who is smart and friendly"
)

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select Model Provider", ["Groq", "OpenAI"])

if provider == "Groq":
    selected_model = st.selectbox("Select Model", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select Model", MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("Allow Web Search")

# Query input
user_query = st.text_area(
    "Enter your query:", 
    placeholder="What is the capital of France?", 
    height=150
)

API_ENDPOINT = "http://127.0.0.1:8000/chat"

col1, col2 = st.columns([1, 1])

with col1:
    ask_button = st.button("Ask Agent!")

with col2:
    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

# Process query
if ask_button and user_query.strip():
    # Add user query to chat history
    st.session_state.chat_history.append({
        "type": "user",
        "content": user_query,
        "timestamp": datetime.now().strftime("%H:%M:%S")
    })
    
    # Make API request
    payload = {
        "model_name": selected_model,
        "model_provider": provider,
        "system_prompt": system_prompt,
        "messages": [user_query],
        "allow_search": allow_web_search
    }
    
    try:
        response = requests.post(API_ENDPOINT, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
                st.session_state.chat_history.append({
                    "type": "error",
                    "content": response_data["error"],
                    "timestamp": datetime.now().strftime("%H:%M:%S")
                })
            else:
                # Add successful response to chat history
                st.session_state.chat_history.append({
                    "type": "assistant",
                    "content": response_data,
                    "timestamp": datetime.now().strftime("%H:%M:%S")
                })
        else:
            error_msg = f"HTTP {response.status_code}: {response.text}"
            st.error(f"API Error: {error_msg}")
            st.session_state.chat_history.append({
                "type": "error",
                "content": error_msg,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.session_state.chat_history.append({
            "type": "error",
            "content": str(e),
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })

# Display chat history
if st.session_state.chat_history:
    st.subheader("Chat History")
    
    for message in reversed(st.session_state.chat_history):
        if message["type"] == "user":
            st.markdown(f"**You ({message['timestamp']}):**")
            st.info(message['content'])
            
        elif message["type"] == "assistant":
            st.markdown(f"**AI Agent ({message['timestamp']}):**")
            st.success(message['content'])
            
        elif message["type"] == "error":
            st.markdown(f"**Error ({message['timestamp']}):**")
            st.error(message['content'])
        
        st.markdown("---")