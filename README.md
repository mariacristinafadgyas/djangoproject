# Django Polls App

This is a small Django project based on the classic **Polls** example app.
It lets you view poll questions at `/polls/`, click a question to see its choices, and manage questions/choices via the Django admin.

## Requirements

- Python 3.x
- pip

Project dependency versions are listed in `requirements.txt`.

## Setup (macOS/Linux)

From the project root (the folder containing `manage.py`):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open:

- App: `http://127.0.0.1:8000/polls/`
- Admin: `http://127.0.0.1:8000/admin/`

## Create an admin user

```bash
source .venv/bin/activate
python manage.py createsuperuser
```

Then log in at `/admin/` and add `Question` + `Choice` entries.

