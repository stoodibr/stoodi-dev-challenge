from django.test import TestCase
from django.db.models.deletion import RestrictedError
from question.models import Question
from user.models import UserHistory


class TestUserHistoryDomainIntegrity(TestCase):
    def setUp(self):
        question = Question.objects.create(text='Foo')

        self.user_history = {
            'question': question,
            'letter': 'a',
            'is_correct': True
        }

        UserHistory.objects.create(**self.user_history)

    def test_letter_max_length(self):
        """SHOULD max_length 1 when column is 'letter'"""

        history = UserHistory.objects.get(id=1)
        max_length = history._meta.get_field('letter').max_length
        self.assertAlmostEqual(max_length, 1)

    def test_on_delete_restrict_throws_exception(self):
        """
            SHOULD raise Exception
            WHEN to try delete a question with related log
        """

        self.assertRaises(
            RestrictedError,
            Question.objects.get(id=1).delete
        )

    def test_model_representation(self):
        """ SHOULD return representantion in pattern:
        {'question', 'letter', 'is_correct', 'datetime' }
        """

        user_history = UserHistory.objects.first()

        repr_result = str(user_history)
        repr_expected = str({
            'user': user_history.user,
            'question': user_history.question.id,
            'letter': user_history.letter,
            'is_correct': user_history.is_correct,
            'datetime': user_history.created_at,
        })

        self.assertEqual(repr_result, repr_expected)
