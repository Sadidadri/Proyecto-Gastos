from django.urls import path

from mainGastos import views

urlpatterns = [
    path('categoria',  views.categoria_list, name='listar_categoria'),
    path('categoria/nueva', views.categoria_create, name='categoria_new'),
    path('categoria/edita/<int:pk>', views.categoria_update, name='categoria_edit'),
    path('categoria/elimina/<int:pk>', views.categoria_delete, name='categoria_delete'),
    path('perfil', views.perfil_list, name='listar_perfil'),
    path('perfil/nuevo', views.perfil_create, name='perfil_new'),
    path('perfil/edita/<int:pk>', views.perfil_update, name='perfil_edit'),
    path('perfil/elimina/<int:pk>', views.perfil_delete, name='perfil_delete'),
    path('l/<int:plk>/gastos/',  views.gasto_list, name='listar_gasto'),
    path('l/<int:plk>/gastos/nuevo', views.gasto_create, name='gasto_new'),
    path('l/<int:plk>/gastos/edita/<int:pk>', views.gasto_update, name='gasto_edit'),
    path('l/<int:plk>/gastos/elimina/<int:pk>', views.gasto_delete, name='gasto_delete'),
]