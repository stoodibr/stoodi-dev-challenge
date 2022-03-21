from django.test import TestCase
from django.contrib import auth
from django.urls import reverse

from user.constants import LOGIN_TEMPLATE, QS_REDIRECT_LOGIN_ERROR
from user.models import CustomUser


class TestUserLoginView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        """SHOULD return HTTP code 200 WHEN access endpoint '/login/' """

        response = self.client.post('/login/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
            SHOULD render template login.html
            WHEN access endpoint '/login/'
        """

        response = self.client.post('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, LOGIN_TEMPLATE)


class TestUseLoginValidationView(TestCase):
    def setUp(self):
        CustomUser.objects.create_user(
            first_name='Foo',
            last_name='Bar',
            email='email@domain.com',
            password='12345'
        )

    def test_view_redirect(self):
        """
            SHOULD return HTTP code 301
            WHEN access endpoint '/login/validacao'
        """
        response = self.client.post('/login/validacao')
        self.assertEqual(response.status_code, 301)

    def test_login_failure_and_redirect_to_login(self):
        """
            SHOULD redirect to '/login/'
            WHEN authenticate fail in '/login/validacao/'
        """

        response = self.client.post('/login/validacao/', data={
            'user_email': 'foo@bar.com',
            'user_password': '12345'
        })

        self.assertRedirects(
            response,
            expected_url=(
                reverse('login')
                + QS_REDIRECT_LOGIN_ERROR['INVALID_LOGIN']
            ),
            status_code=302,
            target_status_code=200
        )

        user = auth.get_user(self.client)

        self.assertFalse(user.is_authenticated)

    def test_login_success_and_redirect_to_login(self):
        """
            SHOULD redirect to '/login/'
            WHEN authenticate successfully in '/login/validacao/'
        """

        response = self.client.post('/login/validacao/', data={
            'user_email': 'email@domain.com',
            'user_password': '12345'
        })

        user = auth.get_user(self.client)

        self.assertRedirects(
            response,
            expected_url=(reverse('question')),
            status_code=302,
            target_status_code=200
        )
        self.assertTrue(user.is_authenticated)
