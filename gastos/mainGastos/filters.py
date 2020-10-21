import django_filters
from .models import Categorias,Gastos,Perfiles

class CategoriaFilter(django_filters.FilterSet):
    class Meta:
        model = Categorias
        fields = ['nombre']
    
class PerfilFilter(django_filters.FilterSet):
    class Meta:
        model = Perfiles
        fields = ['nombre', 'fecha_de_creacion']

class GastoFilter(django_filters.FilterSet):
    class Meta:
        model = Gastos
        fields = ['fk_id_categoria','fk_id_perfil','precio','fecha']