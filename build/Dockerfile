FROM ubuntu:18.04

WORKDIR /opt/src
COPY ./ .

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
   python3 \
   python3-pip

RUN pip3 install -r /opt/src/requirements.txt
