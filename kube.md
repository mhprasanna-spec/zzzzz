# 🚀 TinyLlama Chatbot Deployment on Kubernetes
## 📌 Project Overview

This project deploys a **TinyLlama-based AI chatbot** using:

- Kubernetes

- Ollama

- Streamlit

- NodePort Service

The chatbot runs inside a Kubernetes cluster and is exposed externally using NodePort.

---

## 🧠 Model Used
**Model:** TinyLlama
**Runtime:** Ollama

The model runs inside the Ollama pod.

---

## 🏗️ Architecture

```
Browser
   ↓
NodePort Service
   ↓
Streamlit Pod
   ↓ (ClusterIP Service)
Ollama Pod
   ↓
TinyLlama Model (inside container)

```

