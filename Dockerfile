FROM python:3.13-slim
LABEL org.opencontainers.image.source="https://github.com/Dhiraj123-star/fastapi-monitoring"
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

EXPOSE 8000

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]