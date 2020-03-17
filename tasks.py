from celery import Task, Celery

from clients.dobie_client import send_data_to_dobie

app = Celery('qualichain_mediator')
app.config_from_object('settings', namespace='CELERY_')


@app.task()
def consume_messages_async(message):
    """
    This task is used to received job posting text and feed DOBIE component
    """
    extracted_skills = send_data_to_dobie(message)
    return extracted_skills
