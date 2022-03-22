from django.test import TestCase

from question.models import Question

class TestQuestionView(TestCase):

    def test_answers_ordered(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'question/question.html')
        self.assertEqual(response.context["question"], Question.objects.first())

