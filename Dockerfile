FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /data
WORKDIR /data
COPY requirements.txt /data/
RUN pip install -r requirements.txt
ADD . /data/

