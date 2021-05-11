import time

from django.test import TestCase, Client
from .models import Question

class QuestionTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.question = self.create_question()

    def tearDown(self) -> None:
        self.delete_questions()

    def create_question(self):
        question_1 = Question.objects.create(text="Quanto é 2 + 2 ?")
        question_1.save()
        question_1.insert_option_answer('a', '3')
        question_1.insert_option_answer('c', '5')
        question_1.insert_option_answer('d', '1')
        question_1.insert_option_answer('b', '4', True)
        return question_1

    def delete_questions(self):
        Question.objects.all().delete()

    def test_create_question(self):
        self.assertEqual(self.question.text, 'Quanto é 2 + 2 ?')

    def test_question_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_question_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'question/question.html')

    def test_question_sorted_answers(self):
        ANSWERS = {'a': '3',
                   'b': '4',
                   'c': '5',
                   'd': '1'}
        response = self.client.get('/')
        self.assertEqual(response.context['answers'], ANSWERS)
