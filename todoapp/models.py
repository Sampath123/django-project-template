# Create your models here.
from django.db import models
from django.contrib.auth.models import User

TASK_STATUS = ((0, "Pending"),
               (1, "Completed"))
TASK_PRIORITY = ((0, "High"),
                 (1, "Low"))

TASK_VISIBILITY = ((1, "Private"),
                 (0, "Public"))


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_description = models.CharField(max_length=200)
    task_status = models.IntegerField(choices=TASK_STATUS, default=0)
    task_priority = models.IntegerField(choices=TASK_PRIORITY, default=1)
    task_visibility = models.IntegerField(choices=TASK_VISIBILITY, default=0)
    user_name = models.ForeignKey(User)

    def __unicode__(self):
        return (self.task_name)
