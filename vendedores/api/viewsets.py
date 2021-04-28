from rest_framework.viewsets import ModelViewSet
from vendedores.models import Vendedores
from .serializers import vendedoresSerializer

class vendedoresViewSet(ModelViewSet):
    queryset = Vendedores.objects.all()
    serializer_class = vendedoresSerializer

    filter_fields =('nome','vendedores_cidades')