# Use the official Python 3 base image
FROM python:3

# Set the working directory inside the container
WORKDIR /mlapp

# Copy the requirements file to the working directory
COPY requirements.txt ./

# Copy the model file to the appropriate directory inside the container
COPY model/rental_prediction_model.pkl ./model/rental_prediction_model.pkl

# Copy the application script to the working directory
COPY app.py ./app.py

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the application
EXPOSE 5000

# Define the command to run the application
CMD [ "python", "app.py" ]
