from datetime import date
from pathlib import Path

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from onlinecourse.models import (
    Choice,
    Course,
    Enrollment,
    Instructor,
    Learner,
    Lesson,
    Question,
    Submission,
)


class Command(BaseCommand):
    help = "Create deterministic demo users, course data, questions, and a passing submission."

    def handle(self, *args, **options):
        admin, _ = User.objects.get_or_create(
            username="admin",
            defaults={
                "first_name": "Course",
                "last_name": "Admin",
                "email": "admin@example.com",
                "is_staff": True,
                "is_superuser": True,
            },
        )
        admin.is_staff = True
        admin.is_superuser = True
        admin.set_password("admin123")
        admin.save()

        demo, _ = User.objects.get_or_create(
            username="demo",
            defaults={
                "first_name": "Alex",
                "last_name": "Student",
                "email": "demo@example.com",
            },
        )
        demo.set_password("demo12345")
        demo.save()

        instructor, _ = Instructor.objects.get_or_create(
            user=admin,
            defaults={"full_time": True, "total_learners": 1},
        )
        Learner.objects.get_or_create(
            user=demo,
            defaults={
                "occupation": Learner.DEVELOPER,
                "social_link": "https://github.com/",
            },
        )

        course, _ = Course.objects.get_or_create(
            name="Django Web Development",
            defaults={
                "description": (
                    "A practical introduction to Django models, administration, views, "
                    "templates, routing, and assessment workflows."
                ),
                "pub_date": date(2026, 7, 16),
            },
        )
        course.description = (
            "A practical introduction to Django models, administration, views, "
            "templates, routing, and assessment workflows."
        )
        course.pub_date = date(2026, 7, 16)
        image_path = "media/course_images/django_course.png"
        if Path(image_path).exists():
            course.image = "course_images/django_course.png"
        course.save()
        course.instructors.add(instructor)

        lessons = [
            (
                1,
                "Django Models and ORM",
                "Define Python classes that map to relational database tables. "
                "Use ForeignKey and ManyToManyField relationships to represent courses, "
                "questions, choices, enrollments, and submissions.",
            ),
            (
                2,
                "Admin Site and Inlines",
                "Register models with Django Admin. Inline classes make it possible to "
                "create lessons and questions while editing a course, and choices while "
                "editing a question.",
            ),
            (
                3,
                "Views, Templates, and URLs",
                "Connect URL patterns to view functions. Render course data with Django "
                "template tags and process exam submissions with POST requests and CSRF protection.",
            ),
        ]
        for order, title, content in lessons:
            Lesson.objects.update_or_create(
                course=course,
                order=order,
                defaults={"title": title, "content": content},
            )

        Question.objects.filter(course=course).delete()
        question_data = [
            (
                "Which Django component maps Python classes to database tables?",
                30,
                [("Django ORM", True), ("Template engine", False), ("URL dispatcher", False)],
            ),
            (
                "Which HTTP method should be used to submit the exam form?",
                30,
                [("POST", True), ("GET", False), ("TRACE", False)],
            ),
            (
                "Select the features used by this project.",
                40,
                [
                    ("Django template tags", True),
                    ("Bootstrap styling", True),
                    ("A ManyToManyField for submitted choices", True),
                    ("A React single-page application", False),
                ],
            ),
        ]
        correct_choices = []
        for text, grade, choices in question_data:
            question = Question.objects.create(course=course, text=text, grade=grade)
            for choice_text, is_correct in choices:
                choice = Choice.objects.create(
                    question=question,
                    text=choice_text,
                    is_correct=is_correct,
                )
                if is_correct:
                    correct_choices.append(choice)

        enrollment, _ = Enrollment.objects.get_or_create(
            user=demo,
            course=course,
            defaults={"mode": Enrollment.HONOR, "rating": 5.0},
        )
        course.total_enrollment = Enrollment.objects.filter(course=course).count()
        course.save(update_fields=["total_enrollment"])

        Submission.objects.filter(enrollment=enrollment).delete()
        submission = Submission.objects.create(enrollment=enrollment)
        submission.choices.set(correct_choices)

        self.stdout.write(self.style.SUCCESS("Demo data created successfully."))
        self.stdout.write("Admin: admin / admin123")
        self.stdout.write("Student: demo / demo12345")
        self.stdout.write(f"Course ID: {course.id}; passing submission ID: {submission.id}")
