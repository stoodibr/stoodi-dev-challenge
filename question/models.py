from django.db import models

QUESTION_OPTION_CHOICES = (
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D'),
        ('E', 'Option E')
    )

class Question(models.Model):
    text = models.CharField(max_length=200)
    option_A = models.CharField(max_length=200)
    option_B = models.CharField(max_length=200)
    option_C = models.CharField(max_length=200)
    option_D = models.CharField(max_length=200)
    option_E = models.CharField(max_length=200)

    correct_option = models.CharField(max_length=1, choices=QUESTION_OPTION_CHOICES)

    def get_ordered_options(self):
        return {
            "A": self.option_A,
            "B": self.option_B,
            "C": self.option_C,
            "D": self.option_D,
            "E": self.option_E
        }


