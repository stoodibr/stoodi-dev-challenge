from django.test import TestCase
from django.db.models.deletion import RestrictedError
from question.models import Question
from user.models import CustomUser


class TestCustomUserDomainIntegrity(TestCase):
    def setUp(self):
        self.email = 'foo@bar.com'
        self.password = '12345'

        CustomUser.objects.create(
            email=self.email,
            password=self.password
        )

    def test_exclude_username_from_model(self):
        """SHOUD NOT return username in model"""
        user = CustomUser.objects.filter(email=self.email).values()

        with self.assertRaises(AttributeError):
            user.username

    def test_email_field_is_unique(self):
        """SHOUND return True for email unique field"""
        user = CustomUser.objects.get(email=self.email)
        unique = user._meta.get_field('email').unique

        self.assertTrue(unique)

    def test_model_representation(self):
        """SHOULD return e-mail as representation"""
        user = CustomUser.objects.first()

        self.assertEqual(str(user), self.email)
