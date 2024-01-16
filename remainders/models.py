from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Remainder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=5)
    title = models.CharField(max_length=200)
    detail = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    is_important = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title