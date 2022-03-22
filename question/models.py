from django.db import models

CORRECT_OPTION_CHOICES = (
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D'),
        ('E', 'Option E'),
    )

class Question(models.Model):
    text = models.CharField(max_length=200)
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    option_e = models.CharField(max_length=200)

    correct_option = models.CharField(max_length=1, choices=CORRECT_OPTION_CHOICES)


