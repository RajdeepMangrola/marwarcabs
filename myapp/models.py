from django.db import models

# Create your models here.
class Bookcab(models.Model):
    name = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    cartype = models.CharField(max_length=255)
    pickadd = models.TextField()
    dropadd = models.TextField()
    pickdateandtime = models.DateTimeField()
    
    def __str__(self):
        return self.name