# Flask App - SRE Assignment

## About

This is a simple Flask application that I deployed using Docker and Kubernetes (Minikube).
I made this project to learn how a containerized app works and how Kubernetes manages it.

---

## What I did

* Built a basic Flask app
* Created a Docker image
* Deployed it on Kubernetes
* Added health endpoints
* Exposed it using a service

---

## Tech used

* Python (Flask)
* Docker
* Kubernetes (Minikube)

---

## Project structure

* app.py
* Dockerfile
* requirements.txt
* k8s/deployment.yaml
* k8s/service.yaml

---

## How to run

Start minikube:

minikube start

Use minikube docker:

eval $(minikube docker-env)


Build image:

docker build -t sre-dev-app .

Deploy:

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml


Check pods:

kubectl get pods

Open app:

minikube service flask-service


## Endpoints

* / → basic response
* /health/live → check if app is running
* /health/ready → check if app is ready

---

## Problems I faced

* Minikube was not running at first
* Image not found issue
* YAML mistakes
* Container error due to non-root user

I fixed these by checking logs and using kubectl describe.

---

## What I learned

* Basic Docker usage
* How Kubernetes works (pods and services)
* How to debug errors

---

## GitHub

https://github.com/sumiitjune/sre-assignment
