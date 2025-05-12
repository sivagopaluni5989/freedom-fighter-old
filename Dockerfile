# Use an official Python runtime
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose the port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

