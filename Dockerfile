# Dockerfile

# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Flask application and the score file into the container
COPY MainScores.py /app/
COPY Score.py /app/
COPY Utils.py /app/
COPY Scores.txt /app/

# Install Flask and other required packages
RUN pip install flask

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "MainScores.py"]
