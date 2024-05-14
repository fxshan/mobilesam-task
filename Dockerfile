# Use the official Python image as base
FROM python:3.8

# Set working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y libgl1-mesa-glx

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY . .

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the FastAPI server when the container starts
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
