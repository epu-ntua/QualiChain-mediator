from celery import Task, Celery

app = Celery('qualichain_mediator')
app.config_from_object('settings', namespace='CELERY_')


@app.task()
def consume_messages_async(x):
    print(x, flush=True)
