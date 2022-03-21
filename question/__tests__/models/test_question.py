from django.test import TestCase
from question.models import Question


class TestQuestionModelDomainIntegrity(TestCase):
    def setUp(self):
        self.foo_question = {'text': 'Foo'}
        self.bar_question = {'text': 'Bar'}

        Question.objects.create(**self.foo_question)
        Question.objects.create(**self.bar_question)

    def test_question_text(self):
        """SHOULD return the question text correctly"""

        question1 = Question.objects.get(
            text=self.foo_question.get('text')
        )
        question2 = Question.objects.get(
            text=self.bar_question.get('text')
        )

        self.assertEqual(question1.text, self.foo_question.get('text'))
        self.assertEqual(question2.text, self.bar_question.get('text'))

    def test_text_max_length(self):
        """SHOULD max_length 255 when column is 'text'"""

        question = Question.objects.get(id=1)
        max_length = question._meta.get_field('text').max_length
        self.assertAlmostEqual(max_length, 255)

    def test_representation(self):
        """SHOULD return repr in pattern:
            {question.id} - {question.text}
        """

        expected_repr = '1 - Foo'
        question = str(Question.objects.get(id=1))

        self.assertEqual(question, expected_repr)
