# 🧠 YouTube Video Summarizer
A Langchain framework project that extracts YouTube transcripts (manual or auto-generated), processes them using LangChain, and prepares them for downstream LLM tasks.
---

## 🚀 Features

- ✅ Fetch manually created or auto-generated YouTube transcripts
- 🕒 Only the transcript segment between the timestamps is passed.
- 🧠 Process transcripts with LangChain to provide a summary
- 🖼️ Streamlit-powered web UI for user interaction
- 📁 Clean, modular structure with environment variable support

---

## 🛠 Tech Stack

- **Python 3.10+**
- [LangChain](https://github.com/langchain-ai/langchain)
- [Streamlit](https://streamlit.io/)
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)
- `python-dotenv`

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/langchain-transcript-extractor.git
   cd langchain-transcript-extractor

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

## ⚙️ Environment Variables
   Create a .env file in the root directory and include the following:
   You can use .env.example as a starting point.

---

## 🧪 Usage
   ▶️ Run the Streamlit app:
   streamlit run app.py
   
   This will open a local web app in your browser.

🧠 What You Can Do in the App:
   -Input a YouTube video ID
   -Add the start and end time.
   -Fetch its transcript (manual or auto-generated)
   -Get a summary of the transcript segment

---

🙌 Acknowledgments
   [LangChain](https://github.com/langchain-ai/langchain)
   [Streamlit](https://streamlit.io/)
   [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)
   [OpenAI](https://openai.com/)
