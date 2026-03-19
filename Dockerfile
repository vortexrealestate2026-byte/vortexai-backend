FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN python -m pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
```

And make sure your `celery-beat-scheduler` service has its own start command set in Railway Settings:
```
python -m celery -A src.celery_app beat -l info
