FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /projects

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN apt update
RUN apt-get install git-all -y
RUN apt-get install software-properties-common -y

# # COPY . .
# Esto es para el proyecto de amiami, no en general
WORKDIR /projects
RUN apt-get install wget -y
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz
RUN tar -xvzf geckodriver-v0.29.1-linux64.tar.gz --directory /usr/bin
RUN chmod +x /usr/bin/geckodriver
# install firefox
RUN add-apt-repository ppa:ubuntu-mozilla-security/ppa -y
RUN apt install firefox -y

#

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["tail", "-f", "/dev/null"]
