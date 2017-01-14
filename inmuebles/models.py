from django.db import models

TIPOS_VIVIENDA = sorted([('apartamento', 'Apartamento'), ('casa', 'Casa'), ('otro', 'Otro')])
PROVINCIAS = sorted([('matanzas', 'Matanzas'), ('habana', 'Habana')])
MUNICIPIOS = sorted([('marianao', 'Marianao'), ('playa', 'Playa')])


# Create your models here.
class Inmueble(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    precio = models.PositiveIntegerField()
    direccion = models.CharField(max_length=100, blank=True, default='')
    provincia = models.CharField(choices=PROVINCIAS, max_length=100)
    municipio = models.CharField(choices=MUNICIPIOS, max_length=100)
    descripcion = models.TextField()
    extras = models.TextField()
    #gas_calle = models.BooleanField(default=False)
    #placa_libre = models.BooleanField(default=False)
    #agua_24h = models.BooleanField(default=False)
    #tiene_220 = models.BooleanField(default=False)
    #telefono = models.BooleanField(default=False)
    numero_cuartos = models.PositiveSmallIntegerField()
    area_total = models.PositiveIntegerField()
    tipo = models.CharField(choices=TIPOS_VIVIENDA, max_length=100)
    owner = models.ForeignKey('auth.User', related_name='inmuebles')

    class Meta:
        ordering = ('created',)
