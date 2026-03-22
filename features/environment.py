from django.test import Client

from polls.models import Choice, Question


def before_scenario(context, scenario):
    """Set up the test client and clear the database before each scenario."""
    context.client = Client()
    # Clean up the database to ensure test isolation
    Question.objects.all().delete()
    Choice.objects.all().delete()


def after_scenario(context, scenario):
    """Clean up after each scenario."""
    # The database is cleaned in before_scenario, so no extra cleanup is needed here
    # unless there are other resources to release.
    pass
