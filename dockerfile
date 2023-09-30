# Use the official Python image as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the bot code and dependencies into the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Run your bot script
CMD ["python", "app/memorius.py"]