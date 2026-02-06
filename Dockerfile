FROM python:3.13-slim

# install curl for health checks
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

EXPOSE 8000

LABEL org.opencontainers.image.source="https://github.com/Dhiraj123-star/fastapi-monitoring"

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]