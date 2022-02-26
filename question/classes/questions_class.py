from question.models import Question, Answer

class QuestionsRequest():

    def __init__(self, id = None):
        self.__context = self.__get_questions_context(id)

    def __get_questions_context(self, id_question):

        question = Question.objects.get(id=id_question) if id_question else Question.objects.all()[0]
        answer_list = Answer.objects.filter(question_id=question.id)[:5]
    
        if answer_list:
            return {
                'question_text': question.text,
                'answers': answer_list,
            }
        
        raise ValueError('A pergunta solicitada ainda não está disponível')
    
    def get_context(self):

        return self.__context