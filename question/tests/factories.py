import factory


FACTORY_ORDERED_OPTIONS = {"A": "1", "B": "2", "C": "3", "D": "4", "E": "5"}
CORRECT_OPTION = "B"
WRONG_OPTIONS = ["A", "C", "D", "E"]


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "question.Question"
        django_get_or_create = (
            "text",
            "option_A",
            "option_B",
            "option_C",
            "option_D",
            "option_E",
            "correct_option",
        )

    text = "What is 2 + 2?"
    option_A = "1"
    option_B = "2"
    option_C = "3"
    option_D = "4"
    option_E = "5"

    correct_option = CORRECT_OPTION
