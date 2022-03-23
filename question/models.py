from django.db import models

QUESTION_OPTION_CHOICES = (
    ("A", "Option A"),
    ("B", "Option B"),
    ("C", "Option C"),
    ("D", "Option D"),
    ("E", "Option E"),
)


class Question(models.Model):
    text = models.CharField(
        max_length=200,
        help_text="The question that should be answered. Keep in mind that the question must have only one correct answer.",
    )
    option_A = models.CharField(
        max_length=200,
        help_text="Alternative to answer the question, it will be the first one to be displayed.",
    )
    option_B = models.CharField(
        max_length=200,
        help_text="Alternative to answer the question, it will be the second one to be displayed.",
    )
    option_C = models.CharField(
        max_length=200,
        help_text="Alternative to answer the question, it will be the third one to be displayed.",
    )
    option_D = models.CharField(
        max_length=200,
        help_text="Alternative to answer the question, it will be the fourth one to be displayed.",
    )
    option_E = models.CharField(
        max_length=200,
        help_text="Alternative to answer the question, it will be the fifth one to be displayed.",
    )

    correct_option = models.CharField(
        max_length=1,
        choices=QUESTION_OPTION_CHOICES,
        help_text="This is the letter of the option that contains the question correct answer.",
    )

    def get_ordered_options(self):
        return {
            "A": self.option_A,
            "B": self.option_B,
            "C": self.option_C,
            "D": self.option_D,
            "E": self.option_E,
        }

    def is_option_correct(self, option):
        if option in self.get_ordered_options().keys():
            return option == self.correct_option
        else:
            raise KeyError(
                "Invalid option provided. It should be a value between the options A to E"
            )
