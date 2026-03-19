FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN python -m pip install --no-cache-dir -r requirements.txt
CMD ["python", "-m", "celery", "-A", "src.celery_app", "beat", "-l", "info"]
