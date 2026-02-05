# FastAPI Monitoring

A lightweight boilerplate for a FastAPI application integrated with Prometheus monitoring, Grafana visualization, and Traefik reverse proxy using Docker and Docker Compose.

## 🚀 Features

* **FastAPI**: High-performance Python API.
* **Prometheus**: Real-time monitoring and time-series data collection.
* **Grafana**: Beautiful data visualization and dashboards.
* **Traefik**: Modern reverse proxy with **SSL (HTTPS)** termination.
* **CI/CD**: Automated Docker builds and deployment to **GitHub Container Registry (GHCR)**.
* **Auto-Instrumentation**: Automatically tracks request counts, latencies, and status codes.

## 🛠 Tech Stack

* **Language:** Python 3.13
* **API Framework:** FastAPI
* **Monitoring:** Prometheus
* **Visualization:** Grafana
* **Reverse Proxy:** Traefik v2.11 (with TLS)
* **CI/CD:** GitHub Actions & GHCR

## 🌐 Local DNS & SSL Setup (Ubuntu)

1. **DNS:** Add the following to your `/etc/hosts` file:
```text
127.0.0.1 app.localhost prometheus.localhost grafana.localhost

```


2. **SSL:** Generate self-signed certificates for local HTTPS:
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
docker-compose up -d --build

```


2. **Access the Services (HTTPS):**

| Service | URL | Note |
| --- | --- | --- |
| **FastAPI App** | [https://app.localhost](https://www.google.com/search?q=https://app.localhost) | Secure API Entry |
| **Prometheus UI** | [https://prometheus.localhost](https://www.google.com/search?q=https://prometheus.localhost) | Secure Metrics Query |
| **Grafana** | [https://grafana.localhost](https://www.google.com/search?q=https://grafana.localhost) | Login: `admin` / `admin` |
| **Traefik Dashboard** | [http://localhost:8081](https://www.google.com/search?q=http://localhost:8081) | Proxy Health & Routing |

> **Note:** Since certificates are self-signed, click "Advanced" -> "Proceed" in your browser.

3. **Stop the Stack:**
```bash
docker-compose down

```



## 🤖 CI/CD Deployment

This project automatically builds and pushes a Docker image to GHCR on every push to `main`.

* **Registry Path:** `ghcr.io/Dhiraj123-star/fastapi-monitoring:latest`

---