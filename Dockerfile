# Slim version of Python
FROM python:3.7-slim

WORKDIR /App
COPY . .

# Download Package Information
RUN apt-get update -y

# Install Tkinter and dependecies
RUN apt-get install tk -y
RUN pip install numpy==1.20.0
RUN pip install matplotlib
RUN pip install pyserial


# Commands to run Tkinter application
CMD ["python","App/main.py"]