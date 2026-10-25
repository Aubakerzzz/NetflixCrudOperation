
# Netflix Clone — Kubernetes Manifests

This folder contains Kubernetes resources for:
- PostgreSQL database
- Flask/Gunicorn backend API
- React/Vite frontend served by Nginx

## 1. Build Docker images

Run these commands from your project root:

```bash
docker build -t crudproject-db:latest ./database
docker build -t crudproject-backend:latest ./backend
docker build -t crudproject-frontend:latest ./frontend
```

## 2. Load images into your cluster

For Minikube:

```bash
minikube image load crudproject-db:latest
minikube image load crudproject-backend:latest
minikube image load crudproject-frontend:latest
```

For Kind:

```bash
kind load docker-image crudproject-db:latest
kind load docker-image crudproject-backend:latest
kind load docker-image crudproject-frontend:latest
```

## 3. Configure secrets

Edit `secret.yaml` and replace the development-only credentials before deploying.

Never commit real credentials to Git.

## 4. Deploy Kubernetes resources

Run from the `kubernetes` directory:

```bash
kubectl apply -k .
kubectl get pods -n netflix
kubectl get services -n netflix
kubectl get pvc -n netflix
```

Monitor your pods:

```bash
kubectl get pods -n netflix -w
kubectl logs -n netflix deployment/db
kubectl logs -n netflix deployment/backend
```

## 5. Access the application

For Docker Desktop Kubernetes, try:

http://localhost:30080

Alternatively, use port forwarding:

```bash
kubectl port-forward -n netflix service/frontend 8080:80
```

Open http://localhost:8080.

Test the backend separately:

```bash
kubectl port-forward -n netflix service/backend 5000:5000
```

Open http://127.0.0.1:5000/api/health.

For Minikube, use:

```bash
minikube service frontend -n netflix --url
```

## 6. Docker Compose to Kubernetes mapping

| Docker Compose | Kubernetes |
|---|---|
| Database service | Deployment + ClusterIP Service |
| Backend service | Deployment + ClusterIP Service |
| Frontend service | Deployment + NodePort Service |
| Environment variables | ConfigMap + Secret |
| Named database volume | PersistentVolumeClaim |
| Health checks | Startup, readiness and liveness probes |
| Docker network | Namespace + Service DNS |

## Notes

- Images must exist locally or in a registry accessible to your cluster.
- PostgreSQL storage requires a working storage provisioner.
- The frontend Nginx configuration proxies `/api/` requests to the backend.
- This is a development and learning setup, not a production-ready deployment.
- For production, configure TLS, an Ingress controller, proper secret management, backups, and immutable image tags.
