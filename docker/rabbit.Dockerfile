FROM rabbitmq:alpine

MAINTAINER "marcostaccato@gmail.com"

ADD definitions.json /etc/rabbitmq/
ADD rabbitmq.config /etc/rabbitmq/