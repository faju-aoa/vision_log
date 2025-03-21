
from django.db import models

# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Content(models.Model):
    content = models.OneToOneField(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    def __str__(self):
        return f'{self.text}'







