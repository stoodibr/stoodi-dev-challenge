from django.test import Client, TestCase
from django.urls import reverse

from question.models import Answer, Question


class TestViews(TestCase):

    def setUp(self):
        # setup entities
        question_entity = Question.objects.create(
            id=50, description='Quanto é 2^5?', correct_alternative='d')
        next_question_entity = Question.objects.create(
            id=51, description='Quanto é 5*15?', correct_alternative='a')

        Answer.objects.create(
            alternative='a', description='0', question=question_entity)
        Answer.objects.create(
            alternative='b', description='2', question=question_entity)
        Answer.objects.create(
            alternative='c', description='16', question=question_entity)
        Answer.objects.create(
            alternative='d', description='32', question=question_entity)
        Answer.objects.create(
            alternative='e', description='128', question=question_entity)

        # setup variables
        self.question_id = question_entity.__dict__['id']
        self.next_question_id = next_question_entity.__dict__['id']
        self.not_found_question_id = 4908
        self.correct_alternative = question_entity.__dict__[
            'correct_alternative']
        self.incorrect_alternative = 'a'

        self.client = Client()
        self.list_url = reverse('question')
        self.answer_url = reverse('question_answer')

    def test_questions_GET(self):
        # test
        response = self.client.get(self.list_url)

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'question/question.html')
        self.assertTrue('question_text' in response.context)
        self.assertTrue('answers' in response.context)
        self.assertTrue(len(response.context['answers'].keys()), 5)
        self.assertTrue('question_id' in response.context)
        self.assertTrue(response.context['question_id'], self.question_id)

    def test_questions_POST(self):
        # test
        response = self.client.post(self.list_url, {
            'next_question_id': self.next_question_id
        })

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'question/question.html')
        self.assertTrue('question_text' in response.context)
        self.assertTrue('answers' in response.context)
        self.assertTrue('question_id' in response.context)
        self.assertTrue(response.context['question_id'], self.next_question_id)

    def test_questions_POST_not_found(self):
        response = self.client.post(self.list_url, {
            'question_id': self.not_found_question_id
        })

        self.assertEqual(response.status_code, 404)

    def test_question_answer_POST_valid(self):
        # test
        response = self.client.post(self.answer_url, {
            'question_id': self.question_id,
            'answer': self.correct_alternative
        })

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'question/answer.html')
        self.assertTrue('is_correct' in response.context)
        self.assertTrue(response.context['is_correct'] == True)

    def test_question_answer_POST_invalid(self):
        # test
        response = self.client.post(self.answer_url, {
            'question_id': self.question_id,
            'answer': self.incorrect_alternative
        })

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'question/answer.html')
        self.assertTrue('is_correct' in response.context)
        self.assertTrue(response.context['is_correct'] == False)

    def test_question_answer_POST_next_question(self):
        # test
        response = self.client.post(self.answer_url, {
            'question_id': self.question_id,
            'answer': self.correct_alternative
        })

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'question/answer.html')
        self.assertTrue('next_question_id' in response.context)
        self.assertTrue(
            response.context['next_question_id'], self.next_question_id)

    def test_question_answer_POST_next_question_is_current(self):
        # setup
        Question.objects.filter(id=self.next_question_id).delete()

        # test
        response = self.client.post(self.answer_url, {
            'question_id': self.question_id,
            'answer': self.correct_alternative
        })

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'question/answer.html')

        self.assertTrue('next_question_id' in response.context)
        self.assertTrue(response.context['next_question_id'], self.question_id)
