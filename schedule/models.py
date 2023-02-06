from django.db import models

# Create your models here.

class Schedule(models.Model):
    content = models.TextField()
    date = models.DateField()
    startTime = models.IntegerField()
    endTime = models.IntegerField()
    
    def __str__(self):
        return str(self.date)