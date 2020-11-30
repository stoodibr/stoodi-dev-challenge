# Generated by Django 3.1.1 on 2020-11-30 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_response_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='value',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='response',
            name='is_correct',
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='correct_answer', to='question.answer'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.TextField(help_text='Enunciado da questão.', max_length=3000, verbose_name='Questão'),
        ),
        migrations.AlterField(
            model_name='response',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='question.answer'),
        ),
    ]