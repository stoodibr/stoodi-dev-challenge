from question.models import Question, Answer, CustomLogQuestions

class CustomLogs():
    """ This class must be responsible to manipulate Questions Logs Model """

    def __save_new_log(self, answer, is_correct):    
        log = CustomLogQuestions(selected_answer=answer, is_correct=is_correct)
        log.save()

    def add_log(self, answer, is_correct):
        try:
            self.__save_new_log(answer, is_correct)
        except Exception as e:
            raise Exception(f'Erro ao inserir novo log de resultados. {str(e)}')

    def get_logs_by_user(self):
        pass

