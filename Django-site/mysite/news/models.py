from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length = 128)
    post = models.TextField(default = "")
    date = models.DateTimeField()

    def _str_(self):
        return self.title 
# Create your models here.
