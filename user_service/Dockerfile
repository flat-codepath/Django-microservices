# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy code
COPY . .

# Install dependencies

RUN pip config set global.index-url https://pypi.org/simple
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8001

# Run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
