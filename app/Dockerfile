FROM python:3.12-slim
WORKDIR /app
RUN pip install flask prometheus-flask-exporter
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
