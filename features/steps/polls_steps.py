import datetime
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django

django.setup()

from behave import given, then
from django.utils import timezone

from polls.models import Question


@given("a question published 30 minutes ago")
def step_published_30_min_ago(context):
    context.question = Question(
        question_text="What is BDD?",
        pub_date=timezone.now() - datetime.timedelta(minutes=30),
    )


@given("a question published 2 days ago")
def step_published_2_days_ago(context):
    context.question = Question(
        question_text="Old question",
        pub_date=timezone.now() - datetime.timedelta(days=2),
    )


@given("a question published 1 hour from now")
def step_published_1_hour_from_now(context):
    context.question = Question(
        question_text="Future question",
        pub_date=timezone.now() + datetime.timedelta(hours=1),
    )


@then("it should be considered published recently")
def step_should_be_recent(context):
    assert context.question.was_published_recently() is True


@then("it should not be considered published recently")
def step_should_not_be_recent(context):
    assert context.question.was_published_recently() is False
