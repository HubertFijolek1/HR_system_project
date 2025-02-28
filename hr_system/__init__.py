# This file can remain empty or include Celery app initialization if needed
from .celery import app as celery_app

__all__ = ("celery_app",)
