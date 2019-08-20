#!/usr/bin/env python

import pika
import time


def callback(chan, method, properties, body):
    print("Received {}".format(body))
    chan.basic_ack(delivery_tag=method.delivery_tag)


# Wait for rabbit to start
time.sleep(30)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbit'))

channel = connection.channel()

channel.queue_declare(queue='queue-test', durable=True)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(on_message_callback=callback, queue='queue-test')

print('Waiting for tasks...')

channel.start_consuming()
