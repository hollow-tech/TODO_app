from django.db import models


class Todolist(models.Model):
    task = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task
