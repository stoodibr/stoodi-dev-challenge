from django.test import TestCase

from question.models import Answer, Question


class QuestionViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        question = Question.objects.create(text='Foo')
        question2 = Question.objects.create(text='Bar')

        Answer.objects.create(
            question=question,
            letter='a',
            text='Bar',
            is_correct=True
        )

        Answer.objects.create(
            question=question2,
            letter='a',
            text='Bar',
            is_correct=True
        )

    def test_view_url_exists_at_desired_location(self):
        """SHOULD return HTTP code 200 WHEN access endpoint '/' """

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
            SHOULD render template question/question.html
            WHEN access endpoint '/'
        """

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'question/question.html')

    def test_view_context_render(self):
        """
            SHOULD return question_id, question_text and answers
            WHEN access endpoint '/' and render template
        """

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        self.assertTrue('question_text' in response.context)
        self.assertTrue('answers' in response.context)

    def test_view_context_values(self):
        """SHOULD assert context contains data registered on DB"""

        context_expected = {
            'question_text': 'Foo',
            'answers': {'a': 'Bar'}
        }

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertDictContainsSubset(
            context_expected,
            response.context
        )

    def test_view_when_no_have_questions(self):
        """SHOULD render view template when no have questions"""

        Question.objects.all().delete()

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'question/question.html')
