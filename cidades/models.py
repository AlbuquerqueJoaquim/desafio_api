from django.db import models

# Create your models here.

class Cidades(models.Model):
    id_cidades = models.AutoField(primary_key=True)
    uf = models.CharField(max_length=2)
    nome = models.CharField(max_length=50)


    def __str__(self):
        return self.nome

