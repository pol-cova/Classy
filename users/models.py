from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Model for user details
class Profile(models.Model):
    # Pronouns options
    PRONOUNS = (
        ('SHE', 'She/Her'),
        ('HE', 'He/Him'),
        ('THEY', 'They/Them'),
        ('OTHER', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    pronouns = models.CharField(max_length=5, choices=PRONOUNS, blank=True)
    career = models.CharField(max_length=100, blank=True)
    # check if user is student from cuvalles
    is_cuvalles = models.BooleanField(default=False)
    #profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    # check if profile is complete in a bool
    profile_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    def get_pronoun(self):
        for key, value in self.PRONOUNS:
            if key == self.pronouns:
                return value