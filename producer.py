from clients.rabbitmq_client import RabbitMQClient
import json

if __name__ == "__main__":
    rabbit_mq = RabbitMQClient()

    message = {
        "tasks": [
            {
                "label": "95671c903a5b97a9",
                "jobDescription": "Moving Mobility Forward Aptiv is making mobility real. We are at the forefront of solving mobility toughest challenges. We have the people, experience, know-how and confidence to turn ideas into solutions. Solutions that move our world from what now to what next, while connecting us like never before. To us, nothing is impossible when you have the people with the passion to make anything possible. Mobility has the power to change the world, and we have the power to change mobility. Join our Innovative Team. Want to do more than just imagine the ways our world will move tomorrow? Here your opportunity. Join the technology company that is transforming the future of mobility today. About Aptiv Aptiv is a global technology company that develops safer, greener and more connected solutions, which enable the future of mobility."
            }
        ]
    }
    rabbit_mq.producer(queue='hello', message=json.dumps(message))