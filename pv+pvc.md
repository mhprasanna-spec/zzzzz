🔹 1. PersistentVolume (hostPath)

Create ollama-pv.yaml:
```
nano ollama-pv.yaml
```
```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: ollama-pv
spec:
  capacity:
    storage: 15Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  hostPath:
    path: /mnt/ollama-data
```

Apply:
```
kubectl apply -f ollama-pv.yaml
```
🔹 2. PersistentVolumeClaim

Create ollama-pvc.yaml:
```
nano ollama-pvc.yaml
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
kubectl apply -f ollama-pvc.yaml
```

🔹 3. Ollama Deployment (with local PVC)

Replace your old ollama-deployment.yaml with this:
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
