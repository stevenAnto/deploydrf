from rest_framework import viewsets
from .serializers import ProgrammerSerializar
from .models import Programmer

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializar
# Create your views here.
