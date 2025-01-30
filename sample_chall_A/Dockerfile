# Use a Python base image
FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean

# Set working directory
WORKDIR /app

# Clone the GitHub repository
RUN git clone https://github.com/CTFFramework/docker-challs.git .

# Change directory to the specific challenge folder
WORKDIR /app/sample_chall_A

# Ensure proper permissions
RUN chmod -R 777 /app

# Install necessary Python dependencies
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 80

# Command to run the app
CMD ["python", "app.py"]
