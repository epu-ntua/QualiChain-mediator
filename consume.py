from clients.rabbitmq_client import RabbitMQClient
from settings import APP_QUEUE

if __name__ == "__main__":
    rabbit_mq = RabbitMQClient()
    rabbit_mq.consumer(queue=APP_QUEUE)

