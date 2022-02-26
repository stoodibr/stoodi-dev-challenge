from question.models import Question, Answer

class QuestionsRequest():

    def __init__(self, id = None):
        self.__context = self.__get_questions_context(id)
        self.__current_answer = None

    def __get_questions_context(self, id_question):

        question = Question.objects.get(id=id_question) if Question.objects.filter(id=id_question).exists() else Question.objects.all()[0]
        answer_list = Answer.objects.filter(question_id=question.id)[:5]
    
        if answer_list:
            return {
                'question_text': question.text,
                'answers': answer_list,
            }
        
    def get_next_question_id(self):
        
        if self.__current_answer:
            next_question_id = int(self.__current_answer.question_id.id) + 1
            if Question.objects.filter(id=next_question_id).exists():
                return str(next_question_id)
        
        return Question.objects.all()[0].id

    def get_question_result(self, id_answer):
        if id_answer:
            self.__current_answer =  Answer.objects.get(id=id_answer)
            return self.__current_answer.is_correct
    
    
    def get_current_question(self):
        if self.__current_answer:
            return self.__current_answer.question_id.id
    
    def get_context(self):
        return self.__context