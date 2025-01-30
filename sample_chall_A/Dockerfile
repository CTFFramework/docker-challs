# Use a Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install necessary Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 80

# Command to run the app
CMD ["python", "app.py"]
