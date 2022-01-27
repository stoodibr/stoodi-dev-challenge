from django.test import TestCase
from django.urls import reverse


class TestQuestionView(TestCase):
	def test_view_status(self):
		response = self.client.get(reverse('question:question'))
		text = 'Quanto é 2^5?'
		answers = {
			'a': '0',
			'b': '2',
			'c': '16',
			'd': '32',
			'e': '128',
		}

		self.assertEqual(response.status_code, 200)
		self.assertContains(response.context['question_text'], text)
		self.assertContains(response.context['answers'], answers)
