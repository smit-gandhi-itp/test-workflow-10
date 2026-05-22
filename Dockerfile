FROM python:3.11-slim
LABEL org.opencontainers.image.base.name="python:3.11-slim"
LABEL org.opencontainers.image.title="Math Utility Module"
LABEL org.opencontainers.image.description="Comprehensive mathematical operations module for AGV-186"

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -r appgroup && useradd -r -g appgroup appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir gunicorn>=26.0.0

COPY math.py .
COPY test_math.py .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENV FLASK_APP=math.py
ENV FLASK_DEBUG=0
ENV PYTHONUNBUFFERED=1

RUN chown -R appuser:appgroup /app
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "-m", "unittest", "test_math.py"]