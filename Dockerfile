FROM python:3.7-slim


RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt