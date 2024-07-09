from django.db import models

# Create your models here.
class Team(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='pics')
    position=models.CharField(max_length=20)
    def __str__(self):
        return self.name

