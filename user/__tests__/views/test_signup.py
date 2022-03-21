from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse

from user.models import CustomUser
from user.views import signup_validation
from user.constants import QS_REDIRECT_SIGNUP_ERROR, SIGNUP_TEMPLATE


class TestUserSignupView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        """SHOULD return HTTP code 200 WHEN access endpoint '/cadastro/' """

        response = self.client.post('/cadastro/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
            SHOULD render template signup.html
            WHEN access endpoint '/cadastro/'
        """

        response = self.client.post('/cadastro/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, SIGNUP_TEMPLATE)


class TestUserSignupValidationView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_view_url_exists_at_desired_location(self):
        """SHOULD return HTTP code 301 WHEN access endpoint '/cadastro/' """

        response = self.client.post('/cadastro/validacao')
        self.assertEqual(response.status_code, 301)

    def test_return_general_error_code_in_qs(self):
        qs = signup_validation(None).url.split('/')[-1]
        self.assertEqual(qs, QS_REDIRECT_SIGNUP_ERROR['GENERAL_ERROR'])

    def test_return_required_email_code_in_qs(self):
        request = self.factory.post(
            '/cadastro/validacao',
            data={'user_email': ''}
        )
        qs = signup_validation(request).url.split('/')[-1]
        self.assertEqual(qs, QS_REDIRECT_SIGNUP_ERROR['REQUIRED_EMAIL'])

    def test_return_required_password_code_in_qs(self):
        request = self.factory.post(
            '/cadastro/validacao',
            data={'user_email': 'email@domain.com'}
        )
        qs = signup_validation(request).url.split('/')[-1]
        self.assertEqual(
            qs, QS_REDIRECT_SIGNUP_ERROR['REQUIRED_PASSWORD'])

    def test_return_required_name_code_in_qs(self):
        request = self.factory.post(
            '/cadastro/validacao',
            data={
                'user_email': 'email@domain.com',
                'user_password': '12345'
            }
        )
        qs = signup_validation(request).url.split('/')[-1]
        self.assertEqual(
            qs, QS_REDIRECT_SIGNUP_ERROR['REQUIRED_NAME'])

    def test_return_invalid_email_code_in_qs(self):
        request = self.factory.post(
            '/cadastro/validacao',
            data={
                'user_email': 'foo',
                'user_password': '12345',
                'user_name': 'Foo Bar'
            }
        )
        qs = signup_validation(request).url.split('/')[-1]
        self.assertEqual(
            qs, QS_REDIRECT_SIGNUP_ERROR['INVALID_EMAIL'])

    def test_return_email_already_registered_code_in_qs(self):
        CustomUser.objects.create_user(
            first_name='Foo',
            last_name='Bar',
            email='email@domain.com',
            password='12345'
        )

        request = self.factory.post(
            '/cadastro/validacao',
            data={
                'user_email': 'email@domain.com',
                'user_password': '12345',
                'user_name': 'Foo Bar'
            }
        )
        qs = signup_validation(request).url.split('/')[-1]
        self.assertEqual(
            qs, QS_REDIRECT_SIGNUP_ERROR['EMAIL_ALREADY_REGISTERED'])

    def test_create_user_and_redirect_when_data_is_valid(self):
        payload = {
            'user_email': 'foo@bar.com',
            'user_password': '12345',
            'user_name': 'Foo Bar'
        }

        response = self.client.post(
            reverse('signup_validation'), data=payload)
        user_email = CustomUser.objects.first().email

        self.assertEqual(payload['user_email'], user_email)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            expected_url=reverse('question'),
            status_code=302,
            target_status_code=200
        )
