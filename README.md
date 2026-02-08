# FastAPI Monitoring

A robust boilerplate for a FastAPI application integrated with Prometheus monitoring, Grafana visualization, Loki logging, and PostgreSQL persistence, all behind a Traefik reverse proxy.

## 🚀 Features

* **FastAPI**: High-performance Python API with SQLAlchemy ORM integration.
* **PostgreSQL Persistence**: Reliable data storage using Docker volumes.
* **Full Observability**:
* **Prometheus**: Metrics collection (App + Database).
* **Loki & Promtail**: Centralized log aggregation.
* **Grafana**: Unified dashboards for metrics and logs.


* **Traefik Proxy**: Secure **HTTPS** termination and **Global Auto-Redirect** (HTTP → HTTPS).
* **Health Monitoring**: Native Docker health checks for both the API and Database.
* **CI/CD**: Automated Docker builds pushed to **GitHub Container Registry (GHCR)**.

## 🛠 Tech Stack

* **Language:** Python 3.13
* **API Framework:** FastAPI & SQLAlchemy
* **Database:** PostgreSQL 15
* **Monitoring:** Prometheus, Grafana, Loki, & Postgres Exporter
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
| **FastAPI App** | [https://app.localhost](https://www.google.com/search?q=https://app.localhost) | Secure API & Interactive Docs |
| **Prometheus** | [https://prometheus.localhost](https://www.google.com/search?q=https://prometheus.localhost) | Metrics Query Engine |
| **Grafana** | [https://grafana.localhost](https://www.google.com/search?q=https://grafana.localhost) | Metrics & Logs Dashboard |
| **Traefik Dash** | [http://localhost:8081](https://www.google.com/search?q=http://localhost:8081) | Network & Routing Health |

## 💾 Data Persistence

* **Database:** PostgreSQL runs as a dedicated service.
* **Volumes:** Data is stored in a named Docker volume (`postgres_data`), ensuring it survives container restarts or removals.
* **Monitoring:** A `postgres-exporter` service provides real-time DB stats to Prometheus.

## 🪵 Centralized Logging

Logs are scraped by **Promtail** and pushed to **Loki**:

* **To View Logs:** In Grafana, go to **Explore**, select **Loki**, and use the filter `{container="fastapi-app"}`.

## 🏥 Health Checks

* **App:** Verified via `curl` on `/health` every 30s.
* **Database:** Verified via `pg_isready` utility.
* **Dependency:** The API will wait for the Database to be "Healthy" before starting.

## 🤖 CI/CD Deployment

Every push to the `main` branch builds a new image:

* **Registry Path:** `ghcr.io/Dhiraj123-star/fastapi-monitoring:latest`
* **Auto-Pull:** Docker Compose is configured with `pull_policy: always` to fetch the newest version on every restart.
