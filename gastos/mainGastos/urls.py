from django.urls import path

from mainGastos import views

urlpatterns = [
    path('categoria',  views.FilteredCategoriaListView.as_view(), name='listar_categoria'),
    path('categoria/muestra/<int:pk>', views.categoria_view, name='categoria_view'),
    path('categoria/nueva', views.categoria_create, name='categoria_new'),
    path('categoria/edita/<int:pk>', views.categoria_update, name='categoria_edit'),
    path('categoria/elimina/<int:pk>', views.categoria_delete, name='categoria_delete'),
    path('perfil',  views.FilteredPerfilListView.as_view(), name='listar_perfil'),
    path('perfil/muestra/<int:pk>', views.perfil_view, name='perfil_view'),
    path('perfil/nuevo', views.perfil_create, name='perfil_new'),
    path('perfil/edita/<int:pk>', views.perfil_update, name='perfil_edit'),
    path('perfil/elimina/<int:pk>', views.perfil_delete, name='perfil_delete'),
    path('gasto',  views.FilteredGastoListView.as_view(), name='listar_gasto'),
    path('gasto/muestra/<int:pk>', views.gasto_view, name='gasto_view'),
    path('gasto/nuevo', views.gasto_create, name='gasto_new'),
    path('gasto/edita/<int:pk>', views.gasto_update, name='gasto_edit'),
    path('gasto/elimina/<int:pk>', views.gasto_delete, name='gasto_delete'),
]