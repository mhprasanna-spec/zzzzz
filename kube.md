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
---

## 📦 Kubernetes Components
## 1️⃣ Streamlit Deployment

Frontend UI

Sends user prompts to Ollama service

## 2️⃣ Ollama Deployment

Runs TinyLlama model

Handles AI inference requests

## 3️⃣ Services

Streamlit → NodePort (External access)

Ollama → ClusterIP (Internal communication only)

---

## ⚙️ Deployment Commands

```
kubectl apply -f ollama-deployment.yaml
kubectl apply -f streamlit-deployment.yaml
kubectl apply -f services.yaml
```
## 🔍 Verify Deployment
```
kubectl get pods
kubectl get svc
```



