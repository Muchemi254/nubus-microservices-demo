# README.md

# Nubus Microservices Demo

A demonstration of microservices architecture using Python, Docker, Kubernetes, Helm, and GitLab CI/CD.

## Services

- User Service: Manages user information
- Product Service: Handles product catalog
- Gateway Service: API gateway routing to services

## Prerequisites

- Docker
- Kubernetes cluster (minikube, kind, or cloud provider)
- Helm 3+
- GitLab account (for CI/CD)

## Local Development

1. Start services: `docker-compose up --build`
2. Access gateway at: http://localhost:8000

## Kubernetes Deployment

1. Install with Helm:
   ```bash
   helm install nubus-demo ./helm/nubus-demo -f ./helm/nubus-demo/values-dev.yaml
   ```
