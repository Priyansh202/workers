from django.db import models

# Create your models here.


class Worker(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.TextField()
    contact_info = models.CharField(max_length=20)
    medical_history = models.TextField()
    safety_breaches = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
