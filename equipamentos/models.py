from django.db import models

class Equipamento(models.Model):

    id = models.CharField(max_length=50, primary_key=True)
    nome = models.CharField(max_length=255)
    status = models.BooleanField(default=True)  
    raTitular = models.IntegerField()
    
    def __str__(self):
        return self.nome