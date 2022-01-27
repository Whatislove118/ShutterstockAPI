from .celery import app as celery_app

__all__ = (celery_app, ) # регаем как пространство имен, чтобы при старте джанги celery внедрялся в нее