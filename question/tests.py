from django.test import TestCase, Client
from django.urls import reverse


class TestQuestionView(TestCase):
	def test_view_status(self):
		response = Client().get(reverse('question:question'))
		
		self.assertEquals(response.status_code, 200)

	def test_view_contents(self):
		text = 'Quanto é 2^5?'
		answers = {
			'a': '0',
			'b': '2',
			'c': '16',
			'd': '32',
			'e': '128',
		}
		response = Client().get(reverse('question:question'))
		self.assertContains(response, text)
		self.assertEquals(response.context['answers'], answers)

	# def test_order_of_answers(self):
	# 	response = self.client.get(reverse('question:question'))

