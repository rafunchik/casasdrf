import django_filters
from django_filters.rest_framework import FilterSet
from inmuebles.models import Inmueble


class InmuebleFilter(FilterSet):
    min_precio = django_filters.NumberFilter(name="precio", lookup_expr='gte')
    max_precio = django_filters.NumberFilter(name="precio", lookup_expr='lte')
    min_num_cuartos = django_filters.NumberFilter(name="numero_cuartos", lookup_expr='gte')
    max_num_cuartos = django_filters.NumberFilter(name="numero_cuartos", lookup_expr='lte')
    min_area = django_filters.NumberFilter(name="area_total", lookup_expr='gte')
    max_area = django_filters.NumberFilter(name="area_total", lookup_expr='lte')
    municipios = django_filters.MultipleChoiceFilter(name="municipio", )

    class Meta:
        model = Inmueble
        fields = ['municipios', 'provincia', 'tipo', 'min_precio',
                  'max_precio', 'min_num_cuartos', 'max_num_cuartos', 'min_area', 'max_area']
