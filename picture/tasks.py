from django.conf import settings
from root.celery import app
import redis
import json

def send_message(data):
    data = {'id': data}
    r = redis.StrictRedis(host=settings.REDIS_HOST)
    r.publish("likes_channel", json.dumps(data))
    print('dadasda')
    return 'ok.'

# @app.task
# def add(x, y):
#     return x + y

