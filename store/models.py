from django.db import models

# Create your models here.

class store(models.Model):
    titleproduct = models.CharField(max_length=128) 
    codeproduct = models.CharField(max_length=128)   
    productdescription = models.CharField(max_length=128)
    priceproduct = models.CharField(max_length=128)    
    def __unicode__(self):
        return self.titleproduct
