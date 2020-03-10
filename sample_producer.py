from clients.rabbitmq_client import RabbitMQClient
import json

if __name__ == "__main__":
    rabbit_mq = RabbitMQClient()

    message = {'module': 'dobie', 'data': {'year': 2010}}
    rabbit_mq.producer(queue='hello', message=json.dumps(message))