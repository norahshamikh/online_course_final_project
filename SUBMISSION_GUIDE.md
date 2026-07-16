# What to submit for each assignment item

Before submitting, create a **public GitHub repository** and push the whole project to it. Replace the placeholders below:

- `Eugene8Lost` — your GitHub username;
- `online_course_final_project` — your repository name;
- `main` — normally `main`.

Example base URL:

```text
https://github.com/Eugene8Lost/online_course_final_project/blob/main/
```

## Question 1 — URL, 3 points

**Requirement:** submit the public GitHub URL of `models.py`, containing the `Question`, `Choice`, and `Submission` models.

Submit:

```text
https://github.com/Eugene8Lost/online_course_final_project/blob/main/onlinecourse/models.py
```

Relevant code is near the bottom of `onlinecourse/models.py`.

## Question 2 — URL, 3 points

**Requirement:** submit the public GitHub URL of `admin.py`, containing seven imported model classes and the implementations of `QuestionInline`, `ChoiceInline`, `QuestionAdmin`, and `LessonAdmin`.

Submit:

```text
https://github.com/Eugene8Lost/online_course_final_project/blob/main/onlinecourse/admin.py
```

The file imports exactly these seven classes: `Choice`, `Course`, `Instructor`, `Learner`, `Lesson`, `Question`, and `Submission`.

## Question 3 — screenshot upload, 1 point

**Requirement:** upload a screenshot of the Django Admin site showing the **Authentication and Authorization** section and the **OnlineCourse** section.

Upload this prepared file:

```text
screenshots/03-admin-site.png
```

To recreate it manually:

1. Run `python manage.py runserver`.
2. Open `http://127.0.0.1:8000/admin/`.
3. Sign in with `admin` / `admin123`.
4. Make sure both requested sections are visible.
5. Save the screenshot as `03-admin-site.png`.

## Question 4 — URL, 2 points

**Requirement:** submit the public GitHub URL of `course_details_bootstrap.html`, which displays the course name and all related lessons using Django template tags and Bootstrap styling.

Submit:

```text
https://github.com/Eugene8Lost/online_course_final_project/blob/main/onlinecourse/templates/onlinecourse/course_details_bootstrap.html
```

The template contains Bootstrap classes, `{{ course.name }}`, and loops over `course.lesson_set.all` and `course.question_set.all`.

## Question 5 — URL, 2 points

**Requirement:** submit the public GitHub URL of `views.py`, containing the `submit` and `show_exam_result` functions.

Submit:

```text
https://github.com/Eugene8Lost/online_course_final_project/blob/main/onlinecourse/views.py
```

Search within the file for:

```python
def submit(request, course_id):
```

and:

```python
def show_exam_result(request, course_id, submission_id):
```

## Question 6 — URL, 2 points

**Requirement:** submit the public GitHub URL of `urls.py`, containing the paths for `submit` and `show_exam_result`.

Submit:

```text
https://github.com/Eugene8Lost/online_course_final_project/blob/main/onlinecourse/urls.py
```

The required path names are:

- `submit`;
- `show_exam_result`.

## Question 7 — screenshot upload, 2 points

**Requirement:** upload a screenshot of a successful mock exam attempt showing the **Congratulations** message, score, and exam results.

Upload this prepared file:

```text
screenshots/07-final.png
```

To recreate it manually:

1. Open `http://127.0.0.1:8000/login/`.
2. Sign in with `demo` / `demo12345`.
3. Open the Django Web Development course.
4. Select all correct options:
   - `Django ORM`;
   - `POST`;
   - `Django template tags`;
   - `Bootstrap styling`;
   - `A ManyToManyField for submitted choices`.
5. Click **Submit exam**.
6. Capture the result page with the **Congratulations** message, `100/100`, and answer details.
7. Save it as `07-final.png`.

## Final checklist

- Repository visibility is **Public**.
- Every GitHub URL opens without requiring sign-in.
- You copied a **file URL**, not a local path such as `C:\...`.
- Question 3 uses `screenshots/03-admin-site.png`.
- Question 7 uses `screenshots/07-final.png`.
- Do not submit the ZIP file itself into the URL fields; push its contents to GitHub first.
