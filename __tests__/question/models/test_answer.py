from django.test import TestCase
from question.models import Answer, Question


class AnswerModelDomainIntegrityTest(TestCase):
    def setUp(self):
        question = Question.objects.create(text='Question 1')

        Answer.objects.create(
            question=question,
            letter='a',
            text='Foo',
            is_correct=True
        )

    def test_letter_max_length(self):
        """SHOULD max_length 1 when column is 'letter'"""

        answer = Answer.objects.get(id=1)
        max_length = answer._meta.get_field('letter').max_length
        self.assertAlmostEqual(max_length, 1)

    def test_text_max_length(self):
        """SHOULD max_length 255 when column is 'text'"""

        answer = Answer.objects.get(id=1)
        max_length = answer._meta.get_field('text').max_length
        self.assertAlmostEqual(max_length, 255)

    def test_representation(self):
        """SHOULD return repr in pattern:
            Q{question.id}. ({answer.letter}) {answer.text}
        """

        expected_repr = 'Q1. (a) Foo'
        answer = str(Answer.objects.get(id=1))

        self.assertEqual(answer, expected_repr)


class AnswerModelReferenceIntegrityTest(TestCase):
    def setUp(self):
        self.question = Question.objects.create(text='Quanto é 2+2')

        self.correct_answer = {
            'question': self.question,
            'letter': 'a',
            'text': '4',
            'is_correct': True
        }

        self.incorrect_answer = {
            'question': self.question,
            'letter': 'b',
            'text': '6',
            'is_correct': False
        }

        Answer.objects.create(**self.correct_answer)
        Answer.objects.create(**self.incorrect_answer)

    def test_correct_letter(self):
        """SHOULD return True when answer is correct"""

        is_correct = (
            Answer.objects
            .filter(question=self.question.id)
            .filter(letter=self.correct_answer.get('letter'))
            .values('is_correct').first()
        )

        self.assertTrue(is_correct.get('is_correct'))

    def test_incorrect_letter(self):
        """SHOULD return False when answer is incorrect"""

        is_correct = (
            Answer.objects
            .filter(question=self.question.id)
            .filter(letter=self.incorrect_answer.get('letter'))
            .values('is_correct').first()
        )

        self.assertFalse(is_correct.get('is_correct'))
