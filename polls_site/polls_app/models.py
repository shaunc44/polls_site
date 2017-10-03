import datetime

from django.db import models
from django.utils import timezone
# from django.utils.encoding import python_2


# Create your models here.
# Each variable represents a db field in model
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')

    # __str__ represents django objects in the admin screen and in 
    # the interactive prompt (python3 manage.py shell)
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    # this FK tells Django that each choice is related to a single question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text