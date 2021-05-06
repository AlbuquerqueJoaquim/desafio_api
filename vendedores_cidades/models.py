from django.db import models
from vendedores.models import Vendedores
from cidades.models import Cidades

# Create your models here.
class Vendedores_cidades(models.Model):
    cod_vendedor = models.ForeignKey(Vendedores, on_delete=models.CASCADE)
    cod_cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)

#retornando vendedores e ciddades
    def __str__(self):
        return 'Vendedor-{} ######## Cidade-{}'.format(self.cod_vendedor,self.cod_cidade)

