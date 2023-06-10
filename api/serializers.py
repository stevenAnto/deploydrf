from rest_framework import serializers
from .models import Programmer


class ProgrammerSerializar(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        #Que campos deseo serializar
        #incluye el ID
        fields = '__all__'
