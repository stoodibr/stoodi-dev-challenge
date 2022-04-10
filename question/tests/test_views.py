from django.test import Client, TestCase
from collections import OrderedDict
from django.urls import reverse

from question.models import Answer, Question

class QuestionViewTestCase(TestCase):

    def setUp(self): 
        self.client = Client()
        
        question_entity = Question.objects.create(id=1,description = "Quanto é 2^5?", correct_alternative='d')
        Answer.objects.create(alternative="a", description="0", question=question_entity)
        Answer.objects.create(alternative="b", description="2", question=question_entity)
        Answer.objects.create(alternative="c", description="16", question=question_entity)
        Answer.objects.create(alternative="d", description="32", question=question_entity)
        Answer.objects.create(alternative="e", description="128", question=question_entity)

        question_entity_dict = question_entity.__dict__
        self.question_id = question_entity_dict['id']
        self.correct_alternative = question_entity_dict['correct_alternative']
        self.incorrect_alternative = 'a'

        self.list_url = reverse('question')
        self.answer_url = reverse('question_answer')

    
    def test_questions_GET(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'question/question.html')
        self.assertTrue('question_id' in response.context)
        self.assertTrue('question_text' in response.context)
        self.assertTrue('answers' in response.context)

    def test_question_answer_POST_valid(self):
        response = self.client.post(self.answer_url, {
            'question_id': self.question_id,
            'answer': self.correct_alternative
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'question/answer.html')
        self.assertTrue('is_correct' in response.context)
        self.assertTrue(response.context['is_correct'] == True)

    def test_question_answer_POST_invalid(self):
        response = self.client.post(self.answer_url, {
            'question_id': self.question_id,
            'answer': self.incorrect_alternative
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'question/answer.html')
        self.assertTrue('is_correct' in response.context)
        self.assertTrue(response.context['is_correct'] == False)

