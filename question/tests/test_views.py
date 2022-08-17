from django.test.client import Client
from django.urls import reverse


def test_ordered_answers():
    client = Client()
    url_str = reverse('question')

    data = client.get(url_str)
    answers = data.context['answers']

    ordered_answers = dict(sorted(answers.items()))

    assert  list(ordered_answers.keys()) == list(answers.keys())

