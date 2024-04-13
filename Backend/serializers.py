from .models import *
from rest_framework import serializers

class ZapatosSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Zapatos
        fields = '__all__'

class PantalonesFaldasSerilizer(serializers.ModelSerializer):
    class Meta:
        model = PantalonesFaldas
        fields = '__all__'

class CamisasSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Camisas
        fields = '__all__'

class VestidosSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Vestidos
        fields = '__all__'

class CombinacionesSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Combinaciones
        fields = '__all__'