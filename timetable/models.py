from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
# subject model for timetable: clave, crn , nombre, profesor, aula, horario, color
class Subject(models.Model):
    COLOR_CHOICES = [
        ('#FF0000', 'Rojo'),
        ('#FF7F00', 'Naranja'),
        ('#FFFF00', 'Amarillo'),
        ('#00FF00', 'Verde'),
        ('#0000FF', 'Azul'),
        ('#4B0082', 'Indigo'),
        ('#8F00FF', 'Violeta'),
    ]
    DAY = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miercoles', 'Miercoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sabado', 'Sabado'),
    ]
    # user that create subject
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    clasroom = models.CharField(max_length=50)
    hour_start = models.CharField(max_length=5, validators=[
        RegexValidator(
            regex='^\d{2}:\d{2}$', 
            message='Hour should be in the format HH:MM',
            code='invalid_hour_format'
        )
    ])
    hour_end = models.CharField(max_length=5, validators=[
        RegexValidator(
            regex='^\d{2}:\d{2}$', 
            message='Hour should be in the format HH:MM',
            code='invalid_hour_format'
        )
    ])
    day = models.CharField(max_length=10, choices=DAY, default='Lunes')
    color = models.CharField(max_length=7, choices=COLOR_CHOICES, default='#FF0000')

    def __str__(self):
        return self.name
    
    def get_day(self):
        return self.day
    
    def get_start(self):
        return self.hour_start