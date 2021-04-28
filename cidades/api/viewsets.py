from rest_framework.viewsets import ModelViewSet
from cidades.models import Cidades
from .serializers import cidadesSerializer

class cidadesViewSet(ModelViewSet):
    queryset = Cidades.objects.all()
    serializer_class = cidadesSerializer


