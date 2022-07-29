from django.db import models

from django.db import models

class Familiar(models.Model):
    name= models.CharField(max_length=40)
    last_name= models.CharField(max_length=40)
    edad=models.CharField(max_length=16) 
    creation_date = models.DateField(auto_now_add=True, null=True,blank=True)
    email= models.EmailField()
