from django.db import models
from django.db.models.fields import SlugField

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title