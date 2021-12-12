from django.test import TestCase

from question.models import Question, QuestionChoice

class TestQuestionModel(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.text = 'Question title'

        cls.question = Question.objects.create(
            text=cls.text,
        )
    
    def test_create_question_success(self):
        self.assertIsNotNone(self.question.id)
    
    def test_question_fields(self):
        
        self.assertIsInstance(self.question.text, str)
        self.assertEqual(self.question.text, self.text)


class TestQuestionChoiceModel(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.text = 'Question title'

        cls.question = Question.objects.create(
            text=cls.text,
        )

        cls.answers = [
            QuestionChoice.objects.create(
                question=cls.question,
                text=f'Text option {i}',
                label=f'{chr(ord("A") + i)}'
            ) for i in range(4)
        ]

        cls.question.correct_answer = cls.answers[1]

        cls.question.save()


    def test_create_question_answer_success(self):
        self.assertIsNotNone(self.answers[0].id)


    def test_question_fields(self):
        
        self.assertIsInstance(self.answers[0].text, str)
        self.assertEqual(self.answers[0].text, 'Text option 0')

        self.assertIsInstance(self.answers[0].label, str)
        self.assertEqual(self.answers[0].label, 'A')

        self.assertIsInstance(self.answers[0].question, Question)


    def test_question_choices_relationship(self):
        self.assertEqual(len(self.answers), self.question.answers.count())


    def test_correct_answer_relationship(self):
        self.assertEqual(self.answers[1].answers_question, self.question)
        self.assertEqual(self.question.correct_answer, self.answers[1])
