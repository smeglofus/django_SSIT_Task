import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text



class TimeChoice(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.CharField(max_length=15,primary_key=False)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    vote_count = models.PositiveIntegerField(default=0)







#todo udělat model databáze inspirovanou tímto
#      """SELECT
#     t.time,
#     SUM(CASE WHEN t.choice_id = 1 THEN t.vote_count ELSE 0 END) AS "Choice 1",
#     SUM(CASE WHEN t.choice_id = 2 THEN t.vote_count ELSE 0 END) AS "Choice 2",
#     SUM(CASE WHEN t.choice_id = 3 THEN t.vote_count ELSE 0 END) AS "Choice 3"
# FROM polls_timechoice t
# LEFT JOIN (
#     SELECT id, choice_text FROM polls_choice
# ) c ON t.choice_id = c.id
# GROUP BY t.time"""




