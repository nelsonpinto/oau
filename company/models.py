from django.db import models

# Create your models here.

class client(models.Model):
    company = models.CharField(max_length=128)
    nameproyect = models.CharField(max_length=128)    
    division = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    def __unicode__(self):
        return self.company
    
class document(models.Model):
    namefile = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    revision = models.CharField(max_length=128)
    def __unicode__(self):
        return self.namefile
    
#int = models.IntegerField()
#date = models.DateTimeField()