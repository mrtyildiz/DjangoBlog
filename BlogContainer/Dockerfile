FROM python:latest

RUN apt install -y && apt update -y && apt upgrade -y && apt dist-upgrade 
RUN mkdir -p /app/
COPY requirements.txt /app
RUN pip3 install -r /app/requirements.txt
COPY start.sh /opt
COPY DatabaseCreate.py /opt
