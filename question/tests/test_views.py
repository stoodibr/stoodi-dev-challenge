from django.test import Client, TestCase
from collections import OrderedDict
from django.urls import reverse

class QuestionViewTestCase(TestCase):

    def setUp(self): 
        self.client = Client()
        self.list_url = reverse('question')
        self.answer_url = reverse('question_answer')

    def test_questions_GET(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'question/question.html')
        self.assertTrue('question_text' in response.context)
        self.assertTrue('answers' in response.context)
        self.assertTrue(type(response.context['answers']) == OrderedDict)

    def test_question_answer_POST_valid(self):
        response = self.client.post(self.answer_url, {
            'answer': 'd'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'question/answer.html')
        self.assertTrue('is_correct' in response.context)
        self.assertTrue(response.context['is_correct'] == True)

    def test_question_answer_POST_invalid(self):
        response = self.client.post(self.answer_url, {
            'answer': 'a'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'question/answer.html')
        self.assertTrue('is_correct' in response.context)
        self.assertTrue(response.context['is_correct'] == False)

