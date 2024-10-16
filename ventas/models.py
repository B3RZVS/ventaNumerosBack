from django.db import models

# Create your models here.
class  Oportunidades(models.Model):
    aceptados= models.BooleanField(null= True, blank= True, default=True)
    cantidad= models.IntegerField(default=0)
    empezoConNo= models.BooleanField(default=False, null=True)

