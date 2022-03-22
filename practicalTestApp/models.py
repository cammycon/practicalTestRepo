from django.db import models
from datetime import date

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=128, unique=True)
    startDate = models.DateField("Date")
    description = models.CharField(max_length=600)

    def __str__(self):
        return self.title