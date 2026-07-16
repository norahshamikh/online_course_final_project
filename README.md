# Django Online Course — Final Assessment Project

A complete Django implementation for the Coursera/IBM final project **“Add a New Assessment Feature to an Online Course App.”**

## Included

- `Question`, `Choice`, and `Submission` models;
- Django Admin registration and nested inline editing;
- course details template with lessons, exam form, Django template tags, and Bootstrap;
- `submit` and `show_exam_result` views;
- URL routes for submission and result pages;
- passing/failing score calculation and detailed answer feedback;
- prepared demo data, tests, and submission screenshots;
- `SUBMISSION_GUIDE.md` explaining exactly what to submit for all seven rubric items.

## Quick start

On Windows you can also double-click `run_project.bat`. On macOS/Linux run `./run_project.sh`.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

### macOS/Linux

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Demo credentials

| Purpose | Username | Password |
|---|---|---|
| Django Admin | `admin` | `admin123` |
| Student exam | `demo` | `demo12345` |

The included `db.sqlite3` is already migrated and seeded, so after installing dependencies you can run `python manage.py runserver` immediately. Running `seed_demo` again safely refreshes the demo content.

## Useful pages

- Course list: `http://127.0.0.1:8000/`
- Django Admin: `http://127.0.0.1:8000/admin/`
- Demo course: `http://127.0.0.1:8000/onlinecourse/1/`

## Verification

```bash
python manage.py check
python manage.py test
```
