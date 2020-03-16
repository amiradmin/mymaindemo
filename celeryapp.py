from celery import Celery

app = Celery('tasks',brocker='ampq://guset:guset@172.17.0.2:5672/celery_vhost',backend='rpc://')
