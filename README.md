# LangGraph-AI-Agent  
A modern, end-to-end AI chatbot system that combines LangGraph-based agent orchestration, real-time web search, and an interactive Streamlit frontend. This project empowers users to create context-aware, persona-driven AI agents capable of dynamic reasoning, live fact retrieval, and persistent multi-turn conversations—all backed by FastAPI and large language models.

## 🧠 Overview

This project enables you to:

- Interact with LLM-powered agents using custom personas (e.g., tutor, analyst, researcher)
- Choose between multiple LLM providers (OpenAI, Groq, etc.)
- Integrate real-time web search (via Tavily API)
- Maintain chat history directly in the UI for multi-turn continuity
- Use both streaming and full-response modes
- Explore and test the API via auto-generated docs (Swagger UI)

---

## 🧩 Architecture

### 1. Agent & Tools
- Built with **LangGraph** for agent logic and decision flow
- Supports external tools like **Tavily Search**
- Model flexibility: Easily switch between OpenAI and Groq

### 2. Backend – FastAPI
- `/chat` endpoint receives input, persona, model, and search toggle
- Uses **Pydantic** for strict request/response validation
- Swagger UI (`/docs`) for API testing

### 3. Frontend – Streamlit
- Dropdowns for agent role, model, and search mode
- Styled prompt input area
- Scrollable, session-persistent chat history
- Streaming and non-streaming response display

---

## ✅ Features

- 🔁 **Multi-Turn Memory**: Chat history view for richer conversations
- 🧑‍🎓 **Persona Switching**: Role-based prompts for contextualized responses
- 🌐 **Live Search Toggle**: Use Tavily for real-time fact retrieval
- ⚡ **Streaming Mode**: Watch responses generate in real time
- 🔐 **Type-Safe Communication**: Backend validation with Pydantic
- 🧪 **Interactive API Testing**: Swagger UI included

---

## 📦 Project Structure

```

LangGraph-AI-Agent/
│
├── ai\_agent.py           # LangGraph-based agent logic
├── Backend.py            # FastAPI app with /chat endpoint
├── Frontend.py           # Streamlit UI with chat controls
├── .env.example          # Sample .env file for API keys
├── requirements.txt      # Project dependencies

````

---

## 🚀 Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Yashshah0502/LangGraph-AI-Agent--End-to-End-Web-Connected-Chatbot-with-FastAPI-and-Streamlit.git
   cd LangGraph-AI-Agent--End-to-End-Web-Connected-Chatbot-with-FastAPI-and-Streamlit
````

2. **Set API Keys**

   * Copy `.env.example` to `.env` and add your keys:

     ```
     GROQ_API_KEY=your_groq_key
     OPENAI_API_KEY=your_openai_key
     TAVILY_API_KEY=your_tavily_key
     ```

3. **Install Requirements**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Backend**

   ```bash
   uvicorn Backend:app --reload
   ```

5. **Start the Frontend**

   ```bash
   streamlit run Frontend.py
   ```

6. **(Optional) Test the API**

   * Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 💡 Use Cases

* Personal research and productivity assistants
* Custom language tutors or AI trainers
* Real-time stock, news, or document analyzers
* Developer portfolio demos or LLM experiments
* Educational tools for teaching LLM integrations

---

## 🛠 Technologies Used

| Technology    | Purpose                               |
| ------------- | ------------------------------------- |
| LangGraph     | Agent orchestration and tool chaining |
| FastAPI       | Backend framework                     |
| Pydantic      | Request/response validation           |
| Streamlit     | Frontend UI                           |
| Groq / OpenAI | LLM providers                         |
| Tavily        | Real-time web search integration      |
| Uvicorn       | ASGI server for FastAPI               |

---

## 📌 Best Practices

* Never commit your `.env` file or API keys.
* Use streaming mode for better UX during long responses.
* Explore adding tools or prompts for new personas.
* Consider caching responses for expensive queries.

---

## 🙌 Acknowledgements

* Inspired by modern AI agent orchestration systems
* Built with love using open tools and public APIs

---

**🔗 Repo**: [github.com/Yashshah0502/LangGraph-AI-Agent--End-to-End-Web-Connected-Chatbot-with-FastAPI-and-Streamlit](https://github.com/Yashshah0502/LangGraph-AI-Agent--End-to-End-Web-Connected-Chatbot-with-FastAPI-and-Streamlit)
