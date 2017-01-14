from rest_framework import serializers
from django.contrib.auth.models import User
from inmuebles.models import Inmueble


class InmuebleSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Inmueble
        fields = ('url', 'created', 'direccion', 'provincia', 'municipio', 'descripcion', 'extras', 'numero_cuartos',
                  'area_total', 'tipo', 'owner')
                  
class UserSerializer(serializers.HyperlinkedModelSerializer):
    inmuebles = serializers.HyperlinkedRelatedField(queryset=Inmueble.objects.all(), view_name='inmueble-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'inmuebles')
