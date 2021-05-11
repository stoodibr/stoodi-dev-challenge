from django.db import models


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=255)
    correct_answer = models.ForeignKey('Answer', blank=True, null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def insert_option_answer(self, letter: chr, content: str, is_correct: bool = False):
        answer = Answer.objects.create(question_ref=self,
                                       letter=letter,
                                       content=content)
        answer.save()
        if is_correct:
            self.correct_answer = answer
            self.save()

    def get_answers(self):
        queried_answers = Answer.objects.filter(question_ref=self)
        answers = {answer.letter:answer.content for answer in queried_answers}
        return answers


class Answer(models.Model):
    question_ref = models.ForeignKey('Question', on_delete=models.CASCADE)
    letter = models.CharField(max_length=1, help_text="Answer's Letter Option")
    content = models.TextField(max_length=255, help_text="Text of the answer")

    class Meta:
        unique_together = ('question_ref_id', 'letter')

    def __str__(self):
        return f'{self.letter}: {self.content}'
