# 🤖 SmartAdvisor: Hybrid Chatbot for Personalized Customer Support

## 📌 Overview
SmartAdvisor is an AI-powered hybrid chatbot designed for intelligent customer support. It combines traditional machine learning algorithms like **Decision Trees** and **KNN** with powerful **Generative AI (LLMs)** to deliver context-aware, natural language responses. It can classify rule-based queries, retrieve similar past solutions, and answer open-ended questions using LLMs.

---

## 🚀 Features
- 🔍 **Decision Tree Classifier** for routing predefined support scenarios (e.g., returns, billing).
- 🔗 **KNN Algorithm** to suggest FAQs or solutions based on user similarity.
- 🧠 **Generative AI Integration** with OpenAI GPT or LLaMA for fluid conversation handling.
- 💾 Knowledge base backed by **MongoDB** or **SQLite**.
- 🖥️ Simple **React/Streamlit frontend** with a clean, chat-style interface.

---

## 🧰 Tech Stack
- **Frontend**: React or Streamlit
- **Backend**: FastAPI / Flask, LangChain
- **ML**: Scikit-learn (DecisionTreeClassifier, KNN), Transformers / OpenAI API
- **Database**: MongoDB / SQLite

---

## 📁 Directory Structure
```
smartadvisor-chatbot/
├── backend/
│   ├── app.py                # FastAPI app with endpoints
│   ├── classifier.py         # Decision Tree + KNN logic
│   ├── generative_ai.py      # LLM integration (OpenAI / Hugging Face)
│   └── db.py                 # MongoDB/SQLite connection
├── frontend/
│   └── streamlit_app.py      # Streamlit chat UI (or React frontend)
├── data/
│   └── faqs.csv              # Sample FAQs and training data
├── requirements.txt
└── README.md
```

---

## 🧪 How to Run
### 1. Clone Repo
```bash
git clone https://github.com/yourusername/smartadvisor-chatbot.git
cd smartadvisor-chatbot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Backend
```bash
cd backend
uvicorn app:app --reload
```

### 4. Run Frontend
```bash
cd frontend
streamlit run streamlit_app.py
```

---

## 🧠 Sample Query Flow
```
User: "I want to return a damaged item."
→ Decision Tree: Classifies as Return Request
→ Response: Rule-based support + LLM-generated apology/explanation

User: "Why was my credit card declined?"
→ Decision Tree + KNN: Checks FAQs + returns similar past cases
→ LLM adds clarity with personalized context
```

---

## 📊 Future Enhancements
- Add sentiment/emotion detection for better escalation
- Multi-language support using translation models
- WebSocket integration for live chat feel

---

## 👨‍💻 Author
Built by Rehan Mohammed Qureshi — reach out via [LinkedIn](http://linkedin.com/in/rehanq-tech) or [Email](mailto:rehanq2200@gmail.com)
