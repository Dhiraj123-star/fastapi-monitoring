# FastAPI Monitoring

A lightweight boilerplate for a FastAPI application integrated with Prometheus monitoring, Grafana visualization, and Traefik reverse proxy with automated CI/CD.

## 🚀 Features

* **FastAPI**: High-performance Python API with automated versioning.
* **Prometheus & Grafana**: Full observability stack for real-time metrics.
* **Loki & Promtail**: Centralized log aggregation—view application logs directly in Grafana.
* **Traefik Proxy**: Secure **HTTPS** termination and **Global Auto-Redirect** (HTTP → HTTPS).
* **Health Monitoring**: Native Docker health checks ensuring container readiness before traffic routing.
* **CI/CD**: Automated Docker builds pushed to **GitHub Container Registry (GHCR)**.
* **Auto-Instrumentation**: Out-of-the-box tracking for request counts, latencies, and status codes.

## 🛠 Tech Stack

* **Language:** Python 3.13
* **API Framework:** FastAPI
* **Monitoring:** Prometheus, Grafana, & Loki
* **Reverse Proxy:** Traefik v2.11
* **Automation:** GitHub Actions & GHCR

## 🌐 Local DNS & SSL Setup (Ubuntu)

1. **DNS Configuration:** Add this to your `/etc/hosts`:
```text
127.0.0.1 app.localhost prometheus.localhost grafana.localhost

```


2. **SSL Generation:** Create self-signed certificates for local HTTPS:
```bash
mkdir certs
openssl req -x509 -newkey rsa:4096 -sha256 -days 3650 -nodes \
  -keyout certs/local.key -out certs/local.crt \
  -subj "/CN=*.localhost" \
  -addext "subjectAltName=DNS:app.localhost,DNS:prometheus.localhost,DNS:grafana.localhost"

```



## 🚦 Quick Start

1. **Build and Start:**
```bash
docker-compose up -d

```


2. **Access the Services:**

| Service | URL | Feature |
| --- | --- | --- |
| **FastAPI App** | [https://app.localhost](https://www.google.com/search?q=https://app.localhost) | Secure API (Health Monitored) |
| **Prometheus** | [https://prometheus.localhost](https://www.google.com/search?q=https://prometheus.localhost) | Secure Metrics Explorer |
| **Grafana** | [https://grafana.localhost](https://www.google.com/search?q=https://grafana.localhost) | Metrics & Logs Dashboard |
| **Traefik Dash** | [http://localhost:8081](https://www.google.com/search?q=http://localhost:8081) | Infrastructure Monitoring |

## 🪵 Centralized Logging

Logs are automatically scraped by **Promtail** from Docker and pushed to **Loki**:

* **To View Logs:** In Grafana, go to the **Explore** tab and select **Loki** as the data source.
* **Filter:** Use the label `{container="fastapi-app"}` to see live API logs.

## 🏥 Health Checks

The application includes a self-healing mechanism:

* **Endpoint:** `/health`
* **Docker Logic:** Container is checked every 30s. If it fails 3 times, it is marked `unhealthy` and Traefik stops routing traffic.

## 🤖 CI/CD Deployment

Every push to the `main` branch triggers a GitHub Action build:

* **Registry Path:** `ghcr.io/Dhiraj123-star/fastapi-monitoring:latest`
* **Pull Policy:** Set to `always` in Docker Compose.

---