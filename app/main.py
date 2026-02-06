from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="FastAPI Monitoring Service")

@app.get("/")
async def root():
    return {
        "status":"healthy",
        "version": "2.0.0",
        "source":"Github Container Registry",
        "message":"CI/CD Deployment successful!! Pulled latest from GHCR.",

        }

@app.get("/data")
async def get_data():
    return {"data":[10,20,30,40,50]}

# This line captures request latencies,sizes, and counts automatically
Instrumentator().instrument(app).expose(app)