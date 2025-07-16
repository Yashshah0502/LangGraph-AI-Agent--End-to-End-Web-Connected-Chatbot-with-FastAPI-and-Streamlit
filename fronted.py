import streamlit as st

st.set_page_config(
    page_title="LangGraph AI Agent",
    page_icon=":robot_face:",
    layout="centered",
    )
st.title("LangGraph AI Agent")
st.write("This is a simple AI agent built with LangGraph and FastAPI. You can interact with it using the API endpoint provided below.")

system_prompt = st.text_area("Define you AI Agent: ", height=100, placeholder="Act as an AI chatbot who is smart and friendly")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select Model Provider", ["Groq", "OpenAI"])

if provider == "Groq":
    selected_model = st.selectbox("Select Model", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select Model", MODEL_NAMES_OPENAI)  

allow_we_Search = st.checkbox("Allow Web Search")

user_query = st.text_area("Enter your query:", placeholder="What is the capital of France?" , height=150)

API_ENDPOINT = "http://127.0.0.1:8000/chat"
if st.button("Ask AI Agent"):
    if user_query.strip():
        response = "Hi this is a fixed response"
        st.subheader("Agent Response")
        st.markdown(f"Your response: {response}")

    