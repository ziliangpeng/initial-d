FROM python:3.6-alpine
MAINTAINER Victor Z. Peng

ADD requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ADD . /app

WORKDIR /app

ENTRYPOINT ["python", "web.py"]