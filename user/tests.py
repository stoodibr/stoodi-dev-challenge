from django.test import Client, TestCase

from django.contrib.auth.models import User
from django.urls import reverse


class TestModels(TestCase):
    def setUp(self):
        self.client = Client()
        self.sign_up_url = reverse('sign_up')
        self.sign_in_url = reverse('sign_in')

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

    def test_sign_up_SUCCESS(self):
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

    def test_sign_up_FAIL_user_not_authenticated(self):
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
