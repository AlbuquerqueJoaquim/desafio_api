from rest_framework.serializers import ModelSerializer
from vendedores_cidades.models import Vendedores_cidades
from cidades.api.serializers import cidadesSerializer
from vendedores.api.serializers import vendedoresSerializer

#trazendo os dados
class vendedores_cidadesSerializer(ModelSerializer):
    #trazendo os dados de cidades e vendedor
    cod_cidade = cidadesSerializer(read_only=True)
    cod_vendedor = vendedoresSerializer(read_only=True)
    class Meta:
        model = Vendedores_cidades
        fields = ('cod_vendedor','cod_cidade')

