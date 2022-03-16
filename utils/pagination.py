from question.models import Question

def get_next_question(current_question):
    questions = Question.objects.all()
    question_ids = []
    for question in questions:
        question_ids.append(question.id)
    
    next_question = question_ids.index(int(current_question)) + 1
    if next_question >= question_ids[len(question_ids)-1]:
        return 1
    else:
        return question_ids[next_question]