FROM python:3.11-slim

# Install FFmpeg
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy open-source dependency
COPY --from=ananke-core /ananke-core /ananke-core
RUN pip install -e /ananke-core

# Install proprietary layer
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
