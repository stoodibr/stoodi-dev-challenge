from django.test import Client, TestCase

from django.contrib.auth.models import User
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        # setup variables
        self.client = Client()
        self.sign_up_url = reverse('sign_up')
        self.sign_in_url = reverse('sign_in')
        self.user_log_url = reverse('user_log')

    def test_sign_up_SUCCESS(self):
        # test
        response = self.client.post(self.sign_up_url, {
            'username': "sign_up_success",
            'email': 'sign_up_success@ipsun.com',
            'password': 'sign_up_success'
        })

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/sign_up.html')
        self.assertTrue('success' in response.context)
        self.assertTrue(response.context['success'] == True)

    def test_sign_up_FAIL_user_already_registered(self):
        # setup
        user = User.objects.create_user(
            username='user_already_registered',
            email='user_already_registered@ipsun.com',
            password='user_already_registered'
        )
        user.save()

        # test
        response = self.client.post(self.sign_up_url, {
            'username': "user_already_registered",
            'email': 'user_already_registered@ipsun.com',
            'password': 'user_already_registered'
        })

        # assert
        self.assertEqual(response.status_code, 409)
        self.assertTemplateUsed(response, 'auth/sign_up.html')
        self.assertTrue('success' in response.context)
        self.assertTrue(response.context['success'] == False)

    def test_sign_in_SUCCESS(self):
        # setup
        user = User.objects.create_user(
            username='sign_up_success', email='sign_up_success@ipsun.com', password='sign_up_success')
        user.save()

        # test
        response = self.client.post(self.sign_in_url, {
            'username': "sign_up_success",
            'password': 'sign_up_success'
        })

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/sign_in.html')
        self.assertTrue('success' in response.context)
        self.assertTrue(response.context['success'] == True)

    def test_sign_in_FAIL_user_not_authenticated(self):
        # test
        response = self.client.post(self.sign_in_url, {
            'username': "username_not_registered",
            'password': 'random_password'
        })

        # assert
        self.assertEqual(response.status_code, 401)
        self.assertTemplateUsed(response, 'auth/sign_in.html')
        self.assertTrue('success' in response.context)
        self.assertTrue(response.context['success'] == False)

    def test_list_user_log_SUCCESS(self):
        # setup
        user = User.objects.create_user(
            username='default_username',
            email='default_email@ipsun.com',
            password='default_password'
        )
        user.save()

        # login user
        response = self.client.post(self.sign_in_url, {
            'username': 'default_username',
            'password': 'default_password'
        })

        # test
        response = self.client.post(self.user_log_url)

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log.html')
        self.assertTrue('headers' in response.context)
        self.assertTrue('data' in response.context)

    def test_list_user_log_FAIL_user_not_authenticated(self):
        # logout user
        self.client.logout()

        # test
        response = self.client.post(self.user_log_url)

        # assert
        self.assertEqual(response.status_code, 302)
