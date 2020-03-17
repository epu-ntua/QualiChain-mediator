import json

import pika
from clients.dobie_client import send_data_to_dobie
from settings import RABBITMQ_USER, RABBITMQ_PASSWORD, RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_VHOST
from tasks import consume_messages_async


class RabbitMQClient(object):
    """
    This object is a RabbitMQ Client writter in Python3
    """

    def __init__(self):
        self.user_credentials = pika.PlainCredentials(
            username=RABBITMQ_USER,
            password=RABBITMQ_PASSWORD
        )

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            port=RABBITMQ_PORT,
            virtual_host=RABBITMQ_VHOST,
            credentials=self.user_credentials
        ))

    def producer(self, queue, message):
        """
        This class method is used to produce messages to RabbitMQ

        Args:
            queue: RabbitMQ queue
            message: message to send

        Examples:
            >>> rabbit = RabbitMQClient()
            >>> mydict = {'user': 'guest', 'password': '1234567890'}
            >>> json_data = json.dumps(mydict)
            >>> rabbit.producer(queue='queue', message=json_data)

        """
        channel = self.connection.channel()

        channel.queue_declare(queue=queue)
        channel.basic_publish(exchange='', routing_key=queue, body=message)

        self.connection.close()

    def on_response_callback(self, ch, method, properties, body):
        message = json.loads(body)
        consume_messages_async.delay(message)

    def consumer(self, queue):
        """
        This function is a RabbitMQ Consumer and consumes messages from provided queue

        Args:
            queue: provided queue
        """
        channel = self.connection.channel()

        channel.queue_declare(queue=queue)
        channel.basic_consume(
            queue=queue, on_message_callback=self.on_response_callback, auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C', flush=True)
        channel.start_consuming()
