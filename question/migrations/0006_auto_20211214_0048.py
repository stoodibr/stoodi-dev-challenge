# Generated by Django 3.1.1 on 2021-12-14 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0005_auto_20211213_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(unique=True),
        ),
    ]
