# Use an appropriate base image -> with configuration of your Container / System
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the server file into the container
COPY server.py /app/server.py

# Install any dependencies if needed
RUN pip3 install flask  # Replace with your dependencies
RUN pip3 install openai
# Expose the port your server will run on
EXPOSE 5000

# Define the command to run the server
CMD ["python3", "server.py"]


#Add the environment variable
ENV OPENAI_API_KEY=""
