"""
Behave environment hooks for this Django project.

Django must be configured before importing models or the test client.
`before_scenario` prepares a client (plain `behave`) or uses behave-django's
`context.test.client` when you run `python manage.py behave`.
"""

from __future__ import annotations

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django

django.setup()

from django.conf import settings
from django.test import Client


def before_all(context):
    """Allow Django's test client default host ``testserver`` (Behave / Test Client)."""
    hosts = list(settings.ALLOWED_HOSTS)
    if "testserver" not in hosts:
        settings.ALLOWED_HOSTS = hosts + ["testserver"]


def before_scenario(context, scenario):
    """Fresh DB state and HTTP client for each scenario."""
    from polls.models import Question

    Question.objects.all().delete()

    # behave-django sets `context.test` (Django TestCase) when using:
    #   poetry run python manage.py behave
    if getattr(context, "test", None) is not None:
        context.client = context.test.client
    else:
        context.client = Client()


def after_scenario(context, scenario):
    """Optional teardown; DB is reset in before_scenario."""
    pass


def get_client(context):
    """Return the Django test client from environment or behave-django."""
    if getattr(context, "test", None) is not None:
        return context.test.client
    return context.client
