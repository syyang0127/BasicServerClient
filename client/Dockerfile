# 1. Base image
FROM python:3.9-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy requirements file
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the client source code
COPY . .

# 6. Command to run the client application
CMD ["python", "client.py"]
