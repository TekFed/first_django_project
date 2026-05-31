# First Django Project

A small Django web application built with Django 5.2.6.

## Project Overview

- `first_django_project/` - Django project configuration.
- `blog/` - Django app containing views, templates, static files, and URL routes.
- `db.sqlite3` - SQLite database file (ignored by Git via `.gitignore`).

## Requirements

- Python 3.11+ recommended
- `requirements.txt` is included with pinned dependencies

## Setup

1. Create and activate a Python virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Apply migrations:

```powershell
python manage.py migrate
```

4. Create a superuser (optional):

```powershell
python manage.py createsuperuser
```

## Run the app

```powershell
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` in your browser.

## Notes

- The project uses SQLite by default (`db.sqlite3`).
- Debug mode is enabled in `first_django_project/settings.py`; do not use this configuration in production.
- Static assets and templates for the `blog` app are stored under `blog/static/` and `blog/templates/`.
