from django.test import TestCase
from django.contrib import auth
from django.urls import reverse

from user.constants import QS_REDIRECT_LOGOUT
from user.models import CustomUser


class TestUserLogoutView(TestCase):
    def setUp(self):
        CustomUser.objects.create_user(
            first_name='Foo',
            last_name='Bar',
            email='email@domain.com',
            password='12345'
        )

        self.client.post('/login/validacao/', data={
            'user_email': 'email@domain.com',
            'user_password': '12345'
        })

    def test_view_url_exists_at_desired_location(self):
        """SHOULD return HTTP code 200 WHEN access endpoint '/logout/' """

        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)

    def test_logout_successfully(self):
        """
            SHOULD render template signup.html
            WHEN access endpoint '/cadastro/'
        """
        user = auth.get_user(self.client)

        self.assertTrue(user.is_authenticated)

        response = self.client.get('/logout/')
        self.assertRedirects(
            response,
            expected_url=(
                reverse('login')
                + QS_REDIRECT_LOGOUT['SUCCESS_LOGOUT']
            ),
            status_code=302,
            target_status_code=200
        )

        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)
