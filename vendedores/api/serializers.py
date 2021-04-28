from rest_framework.serializers import ModelSerializer
from vendedores.models import Vendedores
from cidades.api.serializers import cidadesSerializer

#trazendo os dados
class vendedoresSerializer(ModelSerializer):
    #trazendo os dados de cidades em uma relacionaento mantytomany
    vendedores_cidades = cidadesSerializer(many=True)
    class Meta:
        model = Vendedores
        fields = ('id_vendedor','nome','email','status','vendedores_cidades')