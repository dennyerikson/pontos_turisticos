from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontouristicoViewSet(ModelViewSet):

    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
