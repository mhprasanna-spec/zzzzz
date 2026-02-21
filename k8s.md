## Final Kubernetes Architecture
Browser
   ↓
NodePort / Ingress
   ↓
Streamlit Service
   ↓
Streamlit Pod
   ↓ (ClusterIP service)
Ollama Service
   ↓
Ollama Pod
   ↓
Persistent Volume (model storage)
---

We will create:

Ollama Deployment

Ollama Service (ClusterIP)

Persistent Volume for models

Streamlit Deployment

Streamlit Service (NodePort)

STEP 1 — Push Your Streamlit Image (Already Done)

Make sure image exists on DockerHub:

docker push prasanna369/zzzzz_streamlit:latest

🔹 STEP 2 — Create Ollama Persistent Volume

Create file:
```
nano ollama-pv.yaml
```
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: ollama-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 15Gi
```
Apply:
```
kubectl apply -f ollama-pv.yaml
```
🔹 STEP 3 — Ollama Deployment

Create:
```
nano ollama-deployment.yaml
```
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ollama
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ollama
  template:
    metadata:
      labels:
        app: ollama
    spec:
      containers:
        - name: ollama
          image: ollama/ollama:latest
          ports:
            - containerPort: 11434
          volumeMounts:
            - name: ollama-storage
              mountPath: /root/.ollama
      volumes:
        - name: ollama-storage
          persistentVolumeClaim:
            claimName: ollama-pvc
```

Apply:
```
kubectl apply -f ollama-deployment.yaml
```
🔹 STEP 4 — Ollama Service (Internal Only)

Create:
```
nano ollama-service.yaml
```
```
apiVersion: v1
kind: Service
metadata:
  name: ollama
spec:
  selector:
    app: ollama
  ports:
    - port: 11434
      targetPort: 11434
  type: ClusterIP
```

Apply:

kubectl apply -f ollama-service.yaml

Now Ollama is reachable inside cluster at:

http://ollama:11434
🔹 STEP 5 — Streamlit Deployment

Create:

nano streamlit-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: streamlit
spec:
  replicas: 1
  selector:
    matchLabels:
      app: streamlit
  template:
    metadata:
      labels:
        app: streamlit
    spec:
      containers:
        - name: streamlit
          image: prasanna369/zzzzz_streamlit:latest
          ports:
            - containerPort: 8501
          env:
            - name: OLLAMA_HOST
              value: "http://ollama:11434"

Apply:

kubectl apply -f streamlit-deployment.yaml
🔹 STEP 6 — Streamlit Service (Expose to Browser)

Create:

nano streamlit-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: streamlit-service
spec:
  type: NodePort
  selector:
    app: streamlit
  ports:
    - port: 80
      targetPort: 8501
      nodePort: 30007

Apply:

kubectl apply -f streamlit-service.yaml
🔹 STEP 7 — Pull LLaMA Model Inside Ollama Pod

Very important 👇

After ollama pod is running:

kubectl get pods

Find ollama pod name.

Then:

kubectl exec -it <ollama-pod-name> -- ollama pull llama3.2:latest

Wait for model download.

🔹 STEP 8 — Access Application

If EC2:

Open security group:

Allow:

Port 30007

TCP

0.0.0.0/0

Then open:

http://<EC2_PUBLIC_IP>:30007
🔎 Debug Commands

Check everything:

kubectl get pods
kubectl get svc
kubectl logs <streamlit-pod>
kubectl logs <ollama-pod>
