[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/97WR5HaV)

# Kubernetes Flask-PostgreSQL Deployment

This project deploys a Flask-based web app with PostgreSQL on Minikube.

## Steps
1. **Start Minikube:** `minikube start`
2. **Build Flask Docker Image:** `docker build -t flask-app:latest ./app`
3. **Deploy Configs & Services:** `kubectl apply -f manifests/`
4. **Get Flask URL:** `minikube service flask-service --url`
