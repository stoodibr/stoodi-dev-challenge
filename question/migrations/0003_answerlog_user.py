# Generated by Django 4.0.2 on 2022-02-16 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_answerlog_alter_answer_answer_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerlog',
            name='user',
            field=models.CharField(default='Anônimo', max_length=50),
        ),
    ]