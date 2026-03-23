"""
Step definitions for features in ``features/polls_journey.feature`` & ``features/question_recently.feature``.

Requires ``features/environment.py`` to run first (Django setup + client).
"""

from __future__ import annotations

import datetime

from behave import given, then, when
from django.utils import timezone

from features.environment import get_client
from polls.models import Question

# ---------------------------------------------------------------------------
# Feature: Question was_published_recently (in-memory model, no DB)
# ---------------------------------------------------------------------------


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


# ---------------------------------------------------------------------------
# Feature: Polls Application User Journey (Django test client + DB)
# ---------------------------------------------------------------------------


@given('a question "{question_text}" published {days:d} days ago')
def step_question_published_days_ago(context, question_text, days):
    Question.objects.create(
        question_text=question_text,
        pub_date=timezone.now() - datetime.timedelta(days=days),
    )


@given('a question "{question_text}" to be published in {days:d} days')
def step_question_future_days(context, question_text, days):
    Question.objects.create(
        question_text=question_text,
        pub_date=timezone.now() + datetime.timedelta(days=days),
    )


@given('a question "{question_text}" published 1 hour ago')
def step_question_published_1_hour_ago(context, question_text):
    Question.objects.create(
        question_text=question_text,
        pub_date=timezone.now() - datetime.timedelta(hours=1),
    )


@given("there are no questions in the system")
def step_no_questions(context):
    Question.objects.all().delete()


@when("I visit the polls index page")
def step_visit_polls_index(context):
    client = get_client(context)
    context.response = client.get("/polls/")


@then('I should see the text "{text}"')
def step_should_see_text(context, text):
    response = context.response
    if getattr(context, "test", None) is not None:
        context.test.assertContains(response, text)
    else:
        content = response.content.decode()
        assert text in content, f"Expected to find {text!r} in response body"


@then('I should not see the text "{text}"')
def step_should_not_see_text(context, text):
    response = context.response
    if getattr(context, "test", None) is not None:
        context.test.assertNotContains(response, text)
    else:
        content = response.content.decode()
        assert text not in content, f"Expected not to find {text!r} in response body"
