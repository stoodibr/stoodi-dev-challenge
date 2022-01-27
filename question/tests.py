from django.test import TestCase, Client
from django.urls import reverse

question_text = 'Quanto é 2^5?'
question_answers = {
	'a': '0',
	'b': '2',
	'c': '16',
	'd': '32',
	'e': '128',
}

class TestQuestionView(TestCase):
	def test_view_status(self):
		response = Client().get(reverse('question:question'))
		
		self.assertEquals(response.status_code, 200)

	def test_view_contents(self):
		response = Client().get(reverse('question:question'))
		self.assertEquals(response.context['answers'], question_answers)
		self.assertContains(response, question_text)

	def test_order_of_answers(self):
		response = Client().get(reverse('question:question'))
		self.assertEquals(response.context['answers'].keys(), question_answers.keys())

