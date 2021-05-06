from rest_framework.viewsets import ModelViewSet
from vendedores_cidades.models import Vendedores_cidades
from .serializers import vendedores_cidadesSerializer

class Vendedores_cidadesViewSet(ModelViewSet):
    queryset = Vendedores_cidades.objects.all()
    serializer_class = vendedores_cidadesSerializer

    filter_fields =('cod_vendedor','cod_cidade')