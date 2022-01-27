from dataclasses import field
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from .models import Question


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


class QuestionModelTest(TestCase):
	@classmethod
	def setUpClassData(cls):
		# timezone ex: <class 'datetime'> 2022-01-26 19:14:51.076158+00:00
		time = timezone.now()
		Question.objects.create(question_text='Quanto é 2+2?', pub_date=time)

	def test_model_content_question_text(self):
		question = Question.objects.get(id=1)
		field_label = question._meta.get_field('question_text').verbose_name
		self.assertEquals(field_label, 'question_text')
