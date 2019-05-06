#
# 
#
# Use an official Python runtime as a parent image
FROM python:3.7-slim

LABEL MAINTAINER foo@bar.com

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && \
    apt-get install -y build-essential gcc libpq-dev && \
    pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME Universe

# Run app.py when the container launches
ENTRYPOINT python

CMD app.py

