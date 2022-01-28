from django.http import response
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
correct_answer = 'd'

class TestQuestionView(TestCase):
	@classmethod
	def setUpTestData(cls):
		# timezone ex: <class 'datetime'> 2022-01-26 19:14:51.076158+00:00
		time = timezone.now()
		Question.objects.create(
			question_text=question_text, 
			pub_date=time,
			option_a=question_answers['a'],
			option_b=question_answers['b'],
			option_c=question_answers['c'],
			option_d=question_answers['d'],
			option_e=question_answers['e'],
		)

	def test_view_status(self):
		response = Client().get(reverse('question:question'))
		self.assertEquals(response.status_code, 200)

	def test_view_contents(self):
		response = Client().get(reverse('question:question'))
		self.assertContains(response, question_text)
		self.assertEquals(response.context['answers'], question_answers)

	def test_order_of_answers(self):
		response = Client().get(reverse('question:question'))
		self.assertEquals(response.context['answers'].keys(), question_answers.keys())


class TestAnswerView(TestCase):
	@classmethod
	def setUpTestData(cls):
		# timezone ex: <class 'datetime'> 2022-01-26 19:14:51.076158+00:00
		time = timezone.now()
		Question.objects.create(
			question_text=question_text, 
			pub_date=time,
			option_a=question_answers['a'],
			option_b=question_answers['b'],
			option_c=question_answers['c'],
			option_d=question_answers['d'],
			option_e=question_answers['e'],
			correct_answer=correct_answer,
		)

	def test_view_status(self):
		response = Client().get(reverse('question:question_answer'))
		self.assertEquals(response.status_code, 200)


class QuestionModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		# timezone ex: <class 'datetime'> 2022-01-26 19:14:51.076158+00:00
		time = timezone.now()
		Question.objects.create(question_text='Quanto é 2+2?', pub_date=time)

	def test_model_content_question_text(self):
		question = Question.objects.get(id=1)
		field_label = question._meta.get_field('question_text').verbose_name
		self.assertEquals(field_label, 'question text')

