from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Question, QuestionChoice
import pdb

class QuestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionChoice
        exclude = ('id', 'question')

class QuestionRetrieveSerializer(serializers.ModelSerializer):
    correct_answer = serializers.CharField(source='correct_answer.label', read_only=True)
    answers = QuestionChoiceSerializer(many=True)

    class Meta:
        model = Question
        exclude = ('id',)


class QuestionCreateSerializer(serializers.ModelSerializer):
    correct_answer = serializers.CharField()
    answers = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Question
        fields = ('text', 'correct_answer', 'answers',)

    def validate(self, attr):
        ending_label = attr.get('correct_answer', 'A').upper()
        range_diff = ord(ending_label) - ord('A')

        answers = attr.get('answers', [])

        if len(answers) < 2:
            raise ValidationError('The body must have atleast 2 answers')

        if range_diff >= len(answers):
            raise ValidationError(f'There is no option "{ending_label}", either send more answers or change the correct_answer field.')

        return super().validate(attr)


    def create(self, validated_data):
        starting_label = ord('A')
        question = Question.objects.create(text=validated_data['text'])

        for i, answer_text in enumerate(validated_data['answers']):
            current_label = chr(starting_label + i)
            answer = QuestionChoice.objects.create(question=question, text=answer_text, label=current_label)
            question.answers.add(answer)
            if current_label == validated_data['correct_answer']:
                question.correct_answer = answer
                question.save(update_fields=['correct_answer'])
        
        return question
