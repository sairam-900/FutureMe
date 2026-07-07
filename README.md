# 🚀 FutureMe

FutureMe is an AI-powered web application that helps users visualize their future based on their current life details and goals. The application collects user information and uses Google's Gemini AI to generate a personalized future prediction and motivational guidance.

---

## ✨ Features

- 🧑 Enter personal details
- 🎯 Define your future goals
- 📚 Describe your current work or studies
- 📅 Set one-year goals
- 🤖 AI-generated future prediction
- 💡 Personalized motivation and suggestions
- 🌐 Simple and responsive web interface

---

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### AI
- Google Gemini API

---

## 📁 Project Structure

```
FutureMe/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/FutureMe.git
```

### 2. Move into the project folder

```bash
cd FutureMe
```

### 3. Create a virtual environment

Windows

```bash
py -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Environment Variables

Create a `.env` file in the project root.

```
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your own API key.

---

## ▶️ Run the Application

```bash
python main.py
```

or

```bash
py main.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 📝 User Inputs

The application collects:

- Name
- Age
- Present Work / Education
- Future Goal
- One-Year Goal

---

## 🤖 AI Output

FutureMe generates:

- Personalized future prediction
- Career roadmap
- Motivation
- Suggestions for improvement
- Encouraging future vision

---

## 📦 Requirements

- Python 3.10+
- Flask
- python-dotenv
- google-generativeai

Install all requirements using:

```bash
pip install -r requirements.txt
```

---

