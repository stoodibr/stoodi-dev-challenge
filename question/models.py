from django.db import models
import sqlite3

# Create your models here.
class BD(models.Model):
    id = models.AutoField(primary_key=True),
    data = models.DateField(auto_now=True),
    answer_correct = models.CharField(max_length=1)

    def setAnswer(r):
        conn = sqlite3.connect('db.SQLITE3', timeout=10)
        conn.execute("INSERT INTO question_bd(answer_correct) VALUES (?)", (r))
        conn.commit()
        conn.close()

    def getAnswer():
        conn = sqlite3.connect('db.SQLITE3', timeout=10)
        c = conn.cursor()
        result = c.execute("SELECT answer_correct FROM question_bd ORDER BY id DESC LIMIT 1")
        for linha in result.fetchone():
            print(linha)
        return linha

    def __str__(self):
        return self.user.username