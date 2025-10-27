FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Allow platform to set PORT; default to 8080
ENV PORT=8080

# Use gunicorn as the production server and bind to $PORT
CMD ["sh", "-lc", "gunicorn main:app -b 0.0.0.0:${PORT:-8080} --workers 3"]
