FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /task
COPY requirements.txt /task/
RUN pip install -r /task/requirements.txt
COPY . /task/