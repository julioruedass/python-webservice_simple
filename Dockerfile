FROM alpine:3.19

RUN apk add --update python3 py3-pip \
    && pip3 install --upgrade pip 
