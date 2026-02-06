# FastAPI Monitoring

A lightweight boilerplate for a FastAPI application integrated with Prometheus monitoring, Grafana visualization, and Traefik reverse proxy with automated CI/CD.

## 🚀 Features

* **FastAPI**: High-performance Python API with automated versioning.
* **Prometheus & Grafana**: Full observability stack for real-time metrics.
* **Traefik Proxy**: Secure **HTTPS** termination and **Auto-Redirect** (HTTP → HTTPS).
* **CI/CD**: Automated Docker builds pushed to **GitHub Container Registry (GHCR)**.
* **Auto-Update**: Integrated **Watchtower** to automatically pull and deploy the latest GHCR images.
* **Auto-Instrumentation**: Out-of-the-box tracking for request counts, latencies, and status codes.

## 🛠 Tech Stack

* **Language:** Python 3.13
* **API Framework:** FastAPI
* **Monitoring:** Prometheus & Grafana
* **Reverse Proxy:** Traefik v2.11
* **Automation:** GitHub Actions, GHCR, and Watchtower

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
| **FastAPI App** | [https://app.localhost](https://www.google.com/search?q=https://app.localhost) | Secure API (Auto-Redirects from HTTP) |
| **Prometheus** | [https://prometheus.localhost](https://www.google.com/search?q=https://prometheus.localhost) | Secure Metrics Explorer |
| **Grafana** | [https://grafana.localhost](https://www.google.com/search?q=https://grafana.localhost) | Login: `admin` / `admin` |
| **Traefik Dash** | [http://localhost:8081](https://www.google.com/search?q=http://localhost:8081) | Infrastructure Monitoring |

## 🤖 CI/CD & Auto-Deployment

### GitHub Actions

Every push to the `main` branch triggers a build:

* **Target:** `ghcr.io/Dhiraj123-star/fastapi-monitoring:latest`
