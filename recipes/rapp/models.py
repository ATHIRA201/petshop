from django.db import models

# Create your models here.


class re_tbl(models.Model):
    rn = models.CharField(max_length=25)  
    ds = models.TextField()                
    ig = models.CharField(max_length=25) 
    ins = models.TextField() 