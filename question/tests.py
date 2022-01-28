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

	def test_answer_view_status(self):
		response = Client().get(reverse('question:question_answer'))
		self.assertEquals(response.status_code, 200)
    	
	def test_answer_view_content(self):
		response = Client().get(reverse('question:question_answer'))
		self.assertContains(response, 'Resposta errada!')

	# def test_answer_view_correct_answer(self):
	# 	response_post =Client().post('question:question_answer', data=correct_answer)
	# 	self.assertContains(response_post, 'Resposta correta!')

class QuestionModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		# timezone ex: <class 'datetime'> 2022-01-26 19:14:51.076158+00:00
		time = timezone.now()
		Question.objects.create(question_text=question_text, pub_date=time)

	def test_model_content_question_text(self):
		question = Question.objects.get(id=1)
		field_label = question._meta.get_field('question_text').verbose_name
		self.assertEquals(field_label, 'question text')

	def test_model_content_option_a(self):
			question = Question.objects.get(id=1)
			field_label = question._meta.get_field('option_a').verbose_name
			self.assertEquals(field_label, 'option a')

	def test_model_content_option_b(self):
			question = Question.objects.get(id=1)
			field_label = question._meta.get_field('option_b').verbose_name
			self.assertEquals(field_label, 'option b')

	def test_model_content_option_c(self):
			question = Question.objects.get(id=1)
			field_label = question._meta.get_field('option_c').verbose_name
			self.assertEquals(field_label, 'option c')

	def test_model_content_option_d(self):
			question = Question.objects.get(id=1)
			field_label = question._meta.get_field('option_d').verbose_name
			self.assertEquals(field_label, 'option d')

	def test_model_content_option_e(self):
		question = Question.objects.get(id=1)
		field_label = question._meta.get_field('option_e').verbose_name
		self.assertEquals(field_label, 'option e')

	def test_model_content_correct_answer(self):
			question = Question.objects.get(id=1)
			field_label = question._meta.get_field('correct_answer').verbose_name
			self.assertEquals(field_label, 'correct answer')


