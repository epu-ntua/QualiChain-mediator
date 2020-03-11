#!/usr/bin/env bash



echo 'Waiting for RabbitMQ...'

while ! nc -z ${RABBITMQ_HOST} 5672; do

  sleep 0.1

done
echo 'RabbitMQ Initialization completed'

python consume.py