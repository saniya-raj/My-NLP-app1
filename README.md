# 🧠 My NLP App

**Interactive NLP Web App built with Streamlit**

Welcome to **My NLP App**, an elegant, lightweight, and powerful Natural Language Processing application built using Streamlit. This app delivers real-time NLP tasks using locally hosted models — ensuring efficiency, privacy, and smooth performance without external APIs.

---

## 🚀 Features

- 🔐 **User Authentication**  
  Secure login and registration system with hashed password storage.

- 🧠 **Named Entity Recognition (NER)**  
  Detect and highlight named entities (like people, places, organizations) in the input text.

- 📊 **Sentiment Analysis**  
  Analyze whether a sentence expresses **positive**, **negative**, or **neutral** sentiment using local models.

- 🎭 **Emotion Detection**  
  Recognize emotions such as **joy**, **anger**, **sadness**, and more from text.

- 💻 **Streamlit UI**  
  A clean and beautiful frontend, styled with custom CSS .

- ⚡ **Local Models**  
  No API tokens needed — all models are run locally for maximum privacy and speed.

---

## 🧰 Tech Stack

- **Frontend & UI**: Streamlit + Custom CSS  
- **Backend & Logic**: Python, Hugging Face Transformers, Torch  
- **Authentication**: JSON-based user storage with password hashing  
- **Deployment Ready**: Suitable for Streamlit Cloud, Render, or local servers

---

## 📦 Installation & Running

```bash
# Step 1: Clone the repository
git clone https://github.com/saniya-raj/My-NLP-app1.git
cd My-NLP-app1

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the Streamlit app
streamlit run app.py

📁 Project Structure
markdown
Copy
Edit
├── app.py
├── api.py
├── users.json
├── requirements.txt

└── templates/
    ├── emotion_ui.py
    ├── sentiment_ui.py
    └── ner_ui.py
🙌 Contributing
Pull requests and suggestions are welcome! Let’s collaborate to make this app even better.

📬 Contact
Feel free to connect with me on LinkedIn or GitHub.

🌟 Show Some Love
If you like this project, consider giving it a ⭐ on GitHub and sharing it with your network!
