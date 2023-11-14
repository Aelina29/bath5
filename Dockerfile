FROM ubuntu:20.04
# FROM python:3.8
# FROM ultralytics/yolov5

RUN apt-get update && \
   apt-get install --no-install-recommends -y python3 python3-pip libgl1 libglib2.0-0 libsm6 libxrender1 libxext6

WORKDIR /usr/src/app

COPY ./app.py app.py
COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./bath.yaml bath.yaml
RUN mkdir results

CMD ["python3", "./app.py"]
