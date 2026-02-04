# FastAPI Monitoring

A lightweight boilerplate for a FastAPI application integrated with Prometheus monitoring, Grafana visualization, and Traefik reverse proxy using Docker and Docker Compose.

## 🚀 Features

* **FastAPI**: High-performance Python API.
* **Prometheus**: Real-time monitoring and time-series data collection.
* **Grafana**: Beautiful data visualization and dashboards.
* **Traefik**: Modern reverse proxy and load balancer for domain-based routing.
* **Dockerized**: Fully containerized environment for consistent deployment.
* **Auto-Instrumentation**: Automatically tracks request counts, latencies, and status codes.

## 🛠 Tech Stack

* **Language:** Python 3.13
* **API Framework:** FastAPI
* **Monitoring:** Prometheus
* **Visualization:** Grafana
* **Reverse Proxy:** Traefik v2.11
* **Orchestration:** Docker Compose

## 🌐 Local DNS Setup (Ubuntu)

To access the services via domain names, add the following line to your `/etc/hosts` file:

```text
127.0.0.1 app.localhost prometheus.localhost grafana.localhost

```

## 🚦 Quick Start

1. **Build and Start:**

```bash
docker-compose up -d --build

```

2. **Access the Services:**

| Service | URL | Note |
| --- | --- | --- |
| **FastAPI App** | [http://app.localhost](https://www.google.com/search?q=http://app.localhost) | Main API Entry |
| **Metrics Endpoint** | [http://app.localhost/metrics](https://www.google.com/search?q=http://app.localhost/metrics) | Scraped by Prometheus |
| **Prometheus UI** | [http://prometheus.localhost](https://www.google.com/search?q=http://prometheus.localhost) | Query raw metrics |
| **Grafana** | [http://grafana.localhost](https://www.google.com/search?q=http://grafana.localhost) | Login: `admin` / `admin` |
| **Traefik Dashboard** | [http://localhost:8081](https://www.google.com/search?q=http://localhost:8081) | Proxy health & routing |

3. **Stop the Stack:**

```bash
docker-compose down

```

## 📊 Available Metrics

Once running, you can query the following in Prometheus or visualize them in Grafana:

* `http_requests_total`: Total count of HTTP requests.
* `http_request_duration_seconds_count`: Number of requests handled.
* `http_request_size_bytes`: Size of the requests.

---
