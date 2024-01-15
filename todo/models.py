from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    limit_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.title
    

class Group(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=5)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name