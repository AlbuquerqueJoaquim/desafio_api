from django.db import models
from cidades.models import Cidades
# Create your models here.

class Vendedores(models.Model):
    id_vendedor = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    vendedores_cidades = models.ManyToManyField(Cidades)

    def __str__(self):
        return self.nome
