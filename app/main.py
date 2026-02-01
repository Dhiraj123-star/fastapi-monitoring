from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="FastAPI Monitoring Service")

@app.get("/")
async def root():
    return {"status":"healthy","message":"Welcome to the monitored API"}

@app.get("/data")
async def get_data():
    return {"data":[1,2,3,4,5]}

# This line captures request latencies,sizes, and counts automatically
Instrumentator().instrument(app).expose(app)