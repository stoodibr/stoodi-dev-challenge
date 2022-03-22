from django.test import TestCase

class TestQuestionView(TestCase):

    def test_answers_ordered(self):
        sorted_answers = ["a", "b", "c", "d", "e"]
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'question/question.html')
        self.assertEqual(list(response.context["answers"].keys()), sorted_answers)
        self.assertTrue("question_text" in response.context)
