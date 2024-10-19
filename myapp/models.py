from django.db import models

class py5test(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.name