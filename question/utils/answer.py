from question.exceptions.answer import AnswerNotFound
from question.models import Answer


def check_answer(question_id: int, user_input: str) -> bool:
    answer = (
        Answer.objects
        .filter(question=question_id)
        .filter(letter=user_input)
        .values('is_correct')
        .first()
    )

    if answer is None:
        raise AnswerNotFound(
            module='utils',
            scope='answer',
            action='check_answer'
        )

    is_correct = answer.get('is_correct')
    return is_correct
