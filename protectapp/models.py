from django.db import models

# Create your models here.

class protectPy5Test(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.name
