from django.db import models

class Question(models.Model):
    description = models.TextField()
    correct_alternative = models.CharField(max_length=1)

    def get_question(question_id):
        if(question_id):
            return Question.objects.get(id=question_id)
        return Question.objects.first()

    def get_next_question(current_id):
        next_question = (Question.objects
            .filter(id__gt=current_id)
            .exclude(id=current_id)
            .order_by('id').first())

        if(next_question):
            return next_question
        return Question.objects.first()

    def __str__(self):
        return self.description

class Answer(models.Model): 
    alternative = models.CharField(max_length=1)
    description = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


    def list_by_question(question):
        answers_query_set = Answer.objects.filter(question=question).order_by('alternative')

        answers_list = {}
        for answer in answers_query_set.values():
            answers_list[answer['alternative']] = answer['description']

        return answers_list

    def __str__(self):
        return '%s %s' % (self.alternative, self.description)


