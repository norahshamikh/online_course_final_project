from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Choice, Course, Enrollment, Question, Submission


class AssessmentFlowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("student", password="pass12345")
        self.other_user = User.objects.create_user("other", password="pass12345")
        self.course = Course.objects.create(name="Test course", description="Test")
        self.enrollment = Enrollment.objects.create(user=self.user, course=self.course)
        self.question = Question.objects.create(
            course=self.course,
            text="Pick both correct answers",
            grade=100,
        )
        self.correct_one = Choice.objects.create(
            question=self.question, text="A", is_correct=True
        )
        self.correct_two = Choice.objects.create(
            question=self.question, text="B", is_correct=True
        )
        self.wrong = Choice.objects.create(
            question=self.question, text="C", is_correct=False
        )

    def test_question_requires_exact_correct_choice_set(self):
        self.assertTrue(
            self.question.is_get_score([self.correct_one, self.correct_two])
        )
        self.assertFalse(self.question.is_get_score([self.correct_one]))
        self.assertFalse(
            self.question.is_get_score(
                [self.correct_one, self.correct_two, self.wrong]
            )
        )

    def test_course_details_uses_required_template(self):
        response = self.client.get(
            reverse("onlinecourse:course_details", args=[self.course.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "onlinecourse/course_details_bootstrap.html"
        )

    def test_submit_and_show_exam_result(self):
        self.client.login(username="student", password="pass12345")
        response = self.client.post(
            reverse("onlinecourse:submit", args=[self.course.id]),
            {
                f"choice_{self.correct_one.id}": self.correct_one.id,
                f"choice_{self.correct_two.id}": self.correct_two.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        submission = Submission.objects.get(enrollment=self.enrollment)
        result = self.client.get(
            reverse(
                "onlinecourse:show_exam_result",
                args=[self.course.id, submission.id],
            )
        )
        self.assertContains(result, "Congratulations")
        self.assertContains(result, "100")
        self.assertContains(result, "Exam results")

    def test_user_cannot_view_another_users_submission(self):
        submission = Submission.objects.create(enrollment=self.enrollment)
        self.client.login(username="other", password="pass12345")
        response = self.client.get(
            reverse(
                "onlinecourse:show_exam_result",
                args=[self.course.id, submission.id],
            )
        )
        self.assertEqual(response.status_code, 404)
