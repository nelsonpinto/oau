from django.db import models

# Create your models here.

class proyect(models.Model):
    nameproyect = models.CharField(max_length=128)
    stateproyect = models.CharField(max_length=128)    
    company = models.CharField(max_length=128)
    division = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    def __unicode__(self):
        return self.nameproyect