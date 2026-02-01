
# FastAPI Monitoring

A lightweight boilerplate for a FastAPI application integrated with Prometheus monitoring using Docker and Docker Compose.

## 🚀 Features

* **FastAPI**: High-performance Python API.
* **Prometheus**: Real-time monitoring and time-series data collection.
* **Dockerized**: Fully containerized environment for consistent deployment.
* **Auto-Instrumentation**: Automatically tracks request counts, latencies, and status codes.

## 🛠 Tech Stack

* **Language:** Python 3.13
* **API Framework:** FastAPI
* **Monitoring:** Prometheus
* **Orchestration:** Docker Compose

## 🚦 Quick Start

1. **Build and Start:**
```bash
docker-compose up -d --build

```


2. **Access the Services:**
* **FastAPI App:** [http://localhost:8000](https://www.google.com/search?q=http://localhost:8000)
* **Metrics Endpoint:** [http://localhost:8000/metrics](https://www.google.com/search?q=http://localhost:8000/metrics)
* **Prometheus UI:** [http://localhost:9090](https://www.google.com/search?q=http://localhost:9090)


3. **Stop the Stack:**
```bash
docker-compose down

```



## 📊 Available Metrics

Once running, you can query the following in Prometheus:

* `http_requests_total`: Total count of HTTP requests.
* `http_request_duration_seconds_count`: Number of requests handled.
* `http_request_size_bytes`: Size of the requests.

---
