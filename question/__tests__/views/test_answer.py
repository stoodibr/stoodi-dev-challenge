from django.test import TestCase

from question.models import Answer, Question
from question.constants import ANSWER_TEMPLATE


class TestAnswerView(TestCase):
    def setUp(self):
        question = Question.objects.create(text='Foo')

        Answer.objects.create(
            question=question,
            letter='a',
            text='Bar',
            is_correct=True
        )

        self.payload = {
            'question_id': question.id,
            'success': True,
            'answer': 'a'
        }

    def test_view_url_exists_at_desired_location(self):
        """SHOULD return HTTP code 200 WHEN access endpoint '/resposta/' """

        response = self.client.post('/resposta/', data=self.payload)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
            SHOULD render template question/answer.html
            WHEN access endpoint '/resposta'
        """

        response = self.client.post('/resposta/', data=self.payload)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, ANSWER_TEMPLATE)

    def test_view_context_render(self):
        """
            SHOULD return is_correct, success
            WHEN access endpoint '/resposta/' and render template
        """

        response = self.client.post('/resposta/', data=self.payload)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('success' in response.context)
        self.assertTrue('is_correct' in response.context)

    def test_view_context_values(self):
        """SHOULD assert context contains data registered on DB"""

        context_expected = {
            'success': True,
            'is_correct': (
                Answer.objects
                .filter(id=1)
                .values('is_correct')
                .first()
                .get('is_correct')
            )
        }

        response = self.client.post('/resposta/', data=self.payload)

        self.assertEqual(response.status_code, 200)
        self.assertDictContainsSubset(
            context_expected,
            response.context
        )

    def test_view_when_no_have_questions_and_answers(self):
        """SHOULD render view template when no have questions and answers"""

        Question.objects.all().delete()

        response = self.client.get('/resposta/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, ANSWER_TEMPLATE)
