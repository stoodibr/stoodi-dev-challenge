from django.test import TestCase

from question.models import Question
from question.tests.factories import QuestionFactory, factory_ordered_options


class TestQuestionModel(TestCase):
    def test_get_ordered_options(self):
        question = QuestionFactory()
        self.assertEqual(question.get_ordered_options(), factory_ordered_options)

    def test_get_wrong_answer(self):
        question = QuestionFactory()
        self.assertFalse(question.is_option_correct("A"))

    def test_get_right_answer(self):
        question = QuestionFactory()
        self.assertTrue(question.is_option_correct("B"))

    def test_get_invalid_answer(self):
        question = QuestionFactory()
        with self.assertRaises(KeyError):
            question.is_option_correct("Z")


class TestQuestionView(TestCase):
    def test_answers_ordered(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "question/question.html")
        self.assertEqual(response.context["question"], Question.objects.first())
