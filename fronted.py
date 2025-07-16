import streamlit as st

st.set_page_config(
    page_title="LangGraph AI Agent",
    page_icon=":robot_face:",
    layout="wide",)
st.title("LangGraph AI Agent")
st.write("This is a simple AI agent built with LangGraph and FastAPI. You can interact with it using the API endpoint provided below.")

system_prompt = st.text_area("Define you AI Agent: ", height=100, placeholder="Act as an AI chatbot who is smart and friendly")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select Model Provider", ["Groq", "OpenAI"])