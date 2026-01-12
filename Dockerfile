FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY library.py .
COPY test_library.py .

CMD ["python", "library.py"]
