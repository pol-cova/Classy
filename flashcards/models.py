from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Card group model
class CardGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)    
    subject = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    
# Card model
class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_group = models.ForeignKey(CardGroup, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    