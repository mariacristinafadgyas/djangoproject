# Django Polls App

This is a small Django project based on the classic **Polls** example app.
It lets you view poll questions at `/polls/`, click a question to see its choices, and manage questions/choices via the Django admin.

## Requirements

- Python 3.12+ (see `pyproject.toml`)
- [Poetry](https://python-poetry.org/) (dependency manager)

This project uses Poetry (`pyproject.toml` + `poetry.lock`) so setup is consistent across computers.

## Setup (any computer)

From the project root (the folder containing `manage.py`):

If you don't have Poetry installed yet:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Then continue:

```bash
poetry install
poetry run python manage.py migrate
poetry run python manage.py runserver
```

Optional: enter the virtual environment shell (interactive)

```bash
poetry install
poetry shell
python manage.py migrate
python manage.py runserver
```

To exit the shell, type `exit`.

Open:

- App: `http://127.0.0.1:8000/polls/`
- Admin: `http://127.0.0.1:8000/admin/`

## Create an admin user

```bash
poetry run python manage.py createsuperuser
```

Then log in at `/admin/` and add `Question` + `Choice` entries.

