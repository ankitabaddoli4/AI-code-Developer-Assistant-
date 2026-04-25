# 🤖 AI Code Developer Assistant

An AI-powered web application that can generate code, detect bugs, and fix errors automatically.

---

## 🚀 Features

- 🧠 Generate Code from natural language input  
- 🐞 Detect bugs in code  
- 🛠 Automatically fix buggy code  
- 🎯 Clean and interactive UI using Streamlit  
- ⚡ Fallback system (works even without API)  

---

## 🛠 Tech Stack

- Python  
- Streamlit  
- OpenAI API  
- dotenv  

---

## 📂 Project Structure


ai_code_assistant/
│
├── app.py
├── core/
│ ├── generator.py
│ ├── bug_detector.py
│ └── fixer.py
│
├── utils/
│ ├── helpers.py
│ └── prompts.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md


---

## ▶️ How to Run Locally

```bash
# Clone the repo
git clone https://github.com/your-username/ai-code-developer-assistant.git

# Go to project folder
cd ai-code-developer-assistant

# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
🔐 Environment Setup

Create a .env file and add your API key:

OPENAI_API_KEY=your_api_key_here
📸 Screenshots

(Add screenshots of your app here for better presentation)

💡 Future Improvements
💬 Chat-based interface
🌐 Deploy on cloud
🌍 Multi-language support
📊 Code explanation feature

👩‍💻 Author

Ankita Baddoli

