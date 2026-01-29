# Use lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies first (layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY . .

# Expose Flask port
EXPOSE 5000

# Run with Gunicorn (production-ready)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
