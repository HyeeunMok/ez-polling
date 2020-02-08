from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=250)
    published_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Select(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    select_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.select_text
