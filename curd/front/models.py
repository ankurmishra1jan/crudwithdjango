from django.db import models

# Create your models here.
class front(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    number = models.IntegerField()
    img = models.FileField(upload_to='media/')

    def __str__(self):
        return self.name + '-' + self.email