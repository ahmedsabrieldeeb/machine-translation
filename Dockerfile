# Use the official Python base image
FROM python:3.10.4

# Create the working directory
RUN mkdir /app
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt ./requirements.txt

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the entire project directory to the container
COPY . ./

# Expose the port that the Flask app will run on
EXPOSE 8000

# Run the Flask app when the container starts
CMD ["python", "app.py"]