import os

# =================================
#   DOBIE SETTINGS
# =================================
DOBIE_HOST = os.environ.get('DOBIE_HOST', 'localhost')
DOBIE_PORT = os.environ.get('DOBIE_PORT', 9006)

# =================================
#   RABBITMQ SETTINGS
# =================================
RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST', 'localhost')
RABBITMQ_PORT = os.environ.get('RABBITMQ_PORT', 5672)
RABBITMQ_VHOST = os.environ.get('RABBITMQ_VHOST', '/')
RABBITMQ_USER = os.environ.get('RABBITMQ_USER', 'rabbitmq')
RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_PASSWORD', 'rabbitmq')

# =================================
#   APPLICATION SETTINGS
# =================================
APP_QUEUE = os.environ.get('APP_QUEUE', "mediator_queue")

# =================================
#   CELERY SETTINGS
# =================================
CELERY_BROKER_URL = 'pyamqp://{}:{}@{}:{}/{}'.format(
    RABBITMQ_USER, RABBITMQ_PASSWORD, RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_VHOST)

CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_TASK_ACKS_LATE = True
