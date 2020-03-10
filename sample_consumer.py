from clients.rabbitmq_client import RabbitMQClient
if __name__ == "__main__":
    rabbit_mq = RabbitMQClient()
    rabbit_mq.consumer(queue='hello')