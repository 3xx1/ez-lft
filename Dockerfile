# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /ez-lft
WORKDIR /ez-lft

# Copy the current directory contents into the container at /ez-lft
COPY . /ez-lft

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python"]
