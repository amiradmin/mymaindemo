from celery import Celery
from kombu import Queue
app = Celery('tasks',brocker='ampq://guset:guset@172.17.0.2:5672/celery_vhost',backend='rpc://')


app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}
app.conf.timezone = 'UTC'
