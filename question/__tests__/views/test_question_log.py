from django.contrib import auth
from django.test import TestCase

from question.models import Question
from question.constants import QUESTION_LOG_TEMPLATE
from user.models import CustomUser, UserHistory


class TestQuestionLogView(TestCase):
    def setUp(self):
        question = Question.objects.create(text='Foo')
        user = CustomUser.objects.create_user(
            email='foo@bar.com',
            password='12345',
            first_name='Foo',
            last_name='Bar'
        )

        UserHistory.objects.bulk_create([
            UserHistory(user=user, question=question,
                        letter='a', is_correct=True),
            UserHistory(user=user, question=question,
                        letter='b', is_correct=False),
            UserHistory(user=user, question=question,
                        letter='c', is_correct=False),
            UserHistory(user=user, question=question,
                        letter='d', is_correct=False)
        ])

    def test_view_url_exists_at_desired_location(self):
        """
            SHOULD return HTTP code 200
            WHEN access endpoint '/log-questoes/'
        """

        response = self.client.get('/log-questoes/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
            SHOULD render template question/question_log.html
            WHEN access endpoint '/log-questoes/'
        """

        response = self.client.get('/log-questoes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, QUESTION_LOG_TEMPLATE)

    def test_view_when_user_is_authenticated(self):
        """
            SHOULD return a list of UserHitory in history variable
            WHEN user is not authenticated
        """

        self.client.login(username='foo@bar.com',
                          password='12345')

        request = self.client.get('/log-questoes/')
        history_count = (
            UserHistory.objects
            .filter(user=auth.get_user(self.client))
            .count()
        )

        self.assertTrue('history' in request.context)
        self.assertTrue(len(request.context['history']) == history_count)

    def test_view_when_user_is_not_authenticated(self):
        """
            SHOULD return an empty list as history
            WHEN user is not authenticated
        """
        request = self.client.get('/log-questoes/')

        self.assertTrue('history' in request.context)
        self.assertTrue(len(request.context['history']) == 0)
