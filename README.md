# 🤖 AI Chatbot — LangChain + Streamlit

A simple AI-powered chatbot built with **LangChain** at the backend and **Streamlit** at the frontend. The chatbot uses **Google Gemini** as the language model and **LangGraph** to manage the conversation workflow and state.

## ✨ Features

* 💬 Interactive conversational chatbot
* 🧠 Google Gemini LLM integration
* 🔗 LangChain-based backend
* 📊 Streamlit-based frontend
* 🗂️ Conversation state management using LangGraph
* 💾 In-memory conversation checkpointing
* 🔐 API key stored securely using `.env`
* ⚡ Simple and beginner-friendly architecture

## 🛠️ Tech Stack

| Technology    | Purpose                                    |
| ------------- | ------------------------------------------ |
| Python        | Programming language                       |
| LangChain     | LLM application framework                  |
| LangGraph     | Conversation workflow and state management |
| Google Gemini | Large Language Model                       |
| Streamlit     | Frontend / User Interface                  |
| python-dotenv | Environment variable management            |

## 📁 Project Structure

```text
ChatBot/
│
├── ChatBot_Backend.py       # LangChain/LangGraph backend
├── ChatBot_FrontEnd.py                   # Streamlit frontend
├── requirements.txt         # Python dependencies
├── .env                     # API key (not committed)
├── .gitignore               # Ignored files
└── README.md                # Project documentation
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
cd ChatBot
```

### 2. Create a virtual environment

```bash
python -m venv myenv
```

Activate it on Windows:

```powershell
myenv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Get your Gemini API key from **Google AI Studio**.

> ⚠️ Never upload your `.env` file or API key to GitHub.

## ▶️ Running the Application

### Run the backend

```bash
python ChatBot_Backend.py
```

### Run the Streamlit frontend

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

If the `streamlit` command is not recognized, use:

```bash
python -m streamlit run app.py
```

## 🧩 How It Works

```text
          User
           │
           ▼
     Streamlit UI
           │
           ▼
     LangChain
           │
           ▼
       LangGraph
           │
           ▼
     Gemini LLM
           │
           ▼
     AI Response
           │
           ▼
     Streamlit UI
```

The user enters a message through the Streamlit interface. The message is passed to the LangChain/LangGraph backend, where the Gemini model generates a response. The response is then displayed in the Streamlit interface.
### Chatbot Interface

![AI Chatbot Application Preview](image/Screenshot%202026-09-16%20234928.png)

> 💬 A simple AI chatbot interface built with **Streamlit**, powered by **LangChain, LangGraph, and Google Gemini**.

## 🔒 Security

The Gemini API key is loaded using environment variables:

```python
from dotenv import load_dotenv

load_dotenv()
```

The `.env` file should be included in `.gitignore`:

```gitignore
.env
```

## 🚀 Future Improvements

* [ ] Add chat history
* [ ] Add streaming responses
* [ ] Add multiple conversation threads
* [ ] Add document/PDF question answering
* [ ] Add tool calling
* [ ] Add web search
* [ ] Add authentication
* [ ] Deploy the chatbot online

## 👨‍💻 Author

**Shubhankar Mishra**

---

⭐ If you find this project useful, consider giving it a star!
