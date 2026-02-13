
---

## 🌸 LLaMA 3.2 Streamlit Chatbot (Ollama)

A simple **local AI chatbot** built using **Streamlit** and **Ollama**, powered by the `llama3.2:latest` model.
The app runs **fully offline** and includes a **floral background UI**.

---

## 🚀 Features

* 🦙 LLaMA 3.2 running locally via Ollama
* 💬 Chat-style interface (Streamlit)
* ⚡ Streaming responses (real-time typing)
* 🌸 Flower background with readable chat bubbles
* 🔒 No API keys, no internet required

---

## 📁 Project Structure

```
chatbot/
│
├── app.py
├── requirements.txt
├── flowers.jpg
└── README.md
```

---

## 🛠 Prerequisites

* Python **3.9+**
* Ollama installed on your system

👉 Download Ollama: [https://ollama.com](https://ollama.com)

---

## 📦 Installation

### 1️⃣ Create virtual environment (optional but recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Pull the model

```bash
ollama pull llama3.2:latest
```

Make sure Ollama is running:

```bash
ollama run llama3.2:latest
```

---

## ▶ Run the Application

```bash
streamlit run app.py
```

The app will open automatically in your browser.

---

## 🎨 Customization

* Replace `flowers.jpg` with any background image
* Adjust CSS in `app.py` for colors, fonts, or layout
* Change model name if you use another Ollama model

---

## 🧠 Notes

* The `ollama` Python package is a **client only**
* Ollama must be running in the background
* Model downloads are handled by Ollama, not pip

---

## 🙌 Use Cases

* Local AI assistant
* Classroom demos
* Offline chatbot
* AI workshops and training sessions

---

## 📜 License

This project is for **learning and personal use**.
Feel free to modify and extend it.

---



Just tell me 😊
