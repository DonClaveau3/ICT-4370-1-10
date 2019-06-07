from django.db import models

# Create your models here.
class Stock(models.Model):
    """A stock that someone owns"""
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text