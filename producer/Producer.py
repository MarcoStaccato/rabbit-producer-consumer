#!/usr/bin/env python

import pika
import time


def publish(body):
    # send a task
    channel.basic_publish(exchange='',
                          routing_key='queue-test',
                          body=body,
                          properties=pika.BasicProperties(
                              delivery_mode=2  # make task persistent
                          ))


# Wait for rabbit to start
time.sleep(30)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbit'))

channel = connection.channel()

channel.queue_declare(queue='queue-test', durable=True)

while True:
    message = time.time_ns() // 1000
    publish('message number {}'.format(message))
    print('published message {}'.format(message))
    time.sleep(15)
