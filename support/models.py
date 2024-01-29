from django.db import models

# Create your models here.

# ticket model
# name, email, report, date, status
class Ticket(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    report = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name