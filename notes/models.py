from django.db import models
from django.contrib.auth.models import User
from timetable.models import Subject
# Create your models here.
# note model
class Note (models.Model):
    title = models.CharField(max_length=200)
    # add user subjects field
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # add owner field
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # add str method
    def __str__(self):
        return self.title