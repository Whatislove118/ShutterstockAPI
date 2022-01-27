from django.conf import settings
import redis
import json


def publish(id):
    r = redis.Redis(host=settings.REDIS_HOST)
    r.publish("test_channel1")
    