# Generated by Django 3.1.1 on 2022-01-27 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20220127_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(default='correct option', max_length=100),
        ),
    ]
