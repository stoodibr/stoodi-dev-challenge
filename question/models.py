from django.db import models
from django.utils.timezone import now
from django.shortcuts import get_object_or_404


class Question(models.Model):
    description = models.TextField()
    correct_alternative = models.CharField(max_length=1)

    def get_question(question_id=None):
        if(question_id):
            return get_object_or_404(Question, id=question_id)
        return Question.objects.first()

    def get_next_question_id(current_id):
        next_question = (Question.objects
                         .filter(id__gt=current_id)
                         .exclude(id=current_id)
                         .order_by('id').first())

        if(next_question == None):
            next_question = Question.objects.first()

        return next_question.__dict__['id']

    def __str__(self):
        return self.description


class Answer(models.Model):
    alternative = models.CharField(max_length=1)
    description = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def list_by_question(question):
        answers_query_set = Answer.objects.filter(
            question=question).order_by('alternative')

        answers_list = {}
        for answer in answers_query_set.values():
            answers_list[answer['alternative']] = answer['description']

        return answers_list

    def __str__(self):
        return 'Questão %s - Alternativa %s: %s' % (self.question.__dict__['id'],
                                                    self.alternative, self.description)


class LogAnswers(models.Model):
    answer = models.CharField(max_length=1)
    is_correct = models.BooleanField(default=False)
    creation_date = models.DateTimeField(default=now, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return 'Questão %s: %s' % (self.question.__dict__['id'], "Acertou" if self.is_correct else "Errou")
