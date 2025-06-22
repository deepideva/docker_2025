#use simple python base image
FROM python:3.12-slim
WORKDIR /app
COPY main.py .
ENTRYPOINT ["python", "/app/main.py"]
