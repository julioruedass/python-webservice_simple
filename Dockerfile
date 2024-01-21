FROM python:3.9-alpine

RUN apk add --update python3 py3-pip \
    && pip3 install --upgrade pip 

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

CMD [ "python3", "src/python/main.py" ]