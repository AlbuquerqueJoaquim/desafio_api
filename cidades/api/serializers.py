from rest_framework.serializers import ModelSerializer
from cidades.models import Cidades

class cidadesSerializer(ModelSerializer):
    class Meta:
        model = Cidades
        fields= ('id_cidades','uf','nome')