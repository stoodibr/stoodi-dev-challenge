from multiprocessing.connection import answer_challenge
from django.db import models

class Question(models.Model):
	answers_option = [
    ('a', 'a'),
    ('b', 'b'),
    ('c', 'c'),
		('d', 'd'),
		('e', 'e'),
	]
	question_text = models.CharField(max_length=200)
	pub_date = models.DateField('date published')
	option_a = models.CharField(max_length=100, default='option' )
	option_b = models.CharField(max_length=100, default='option' )
	option_c = models.CharField(max_length=100, default='option' )
	option_d = models.CharField(max_length=100, default='option' )
	option_e = models.CharField(max_length=100, default='option' )
	correct_answer = models.CharField(max_length=100, choices=answers_option)


	def __str__(self):
		return self.question_text
