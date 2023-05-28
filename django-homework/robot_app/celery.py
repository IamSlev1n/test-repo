import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robot_app.settings')

app = Celery('robot_app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'user_qty_schedule': {
        'task': 'user.tasks.users_count',
        'schedule': 60,
        'args': (),
        'kwargs': {},
    }
}