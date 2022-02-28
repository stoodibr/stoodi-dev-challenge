from .base_model import BaseModel
from question.models import CustomLogQuestions

class CustomLogsClassTestCases(BaseModel):

    def test_customlogs_method_add_log(self):
        
        self.logger.add_log(self.answer_true.text, str(self.answer_true.is_correct), self.user)
        expected_last_log = CustomLogQuestions.objects.all().latest('id')

        self.assertEquals(expected_last_log.selected_answer, self.answer_true.text)
        self.assertEquals(expected_last_log.is_correct, str(self.answer_true.is_correct))

    def test_customlogs_method_get_log_by_user(self):

        expected_user_logs = self.logger.get_logs_by_user(self.user.id)
        query_user_logs = CustomLogQuestions.objects.filter(user=self.user.id)

        self.assertEquals(len(expected_user_logs['logs']), len(query_user_logs))





