from django.urls import path

from mainGastos import views

urlpatterns = [
    path('categoria',  views.FilteredCategoriaListView.as_view(), name='listar_categoria'),
    #path('telephone/view/<int:pk>', views.telephone_view, name='telephone_view'),
    #path('telephone/new', views.telephone_create, name='telephone_new'),
    #path('telephone/edit/<int:pk>', views.telephone_update, name='telephone_edit'),
    #path('telephone/delete/<int:pk>', views.telephone_delete, name='telephone_delete'),
    path('perfil',  views.FilteredPerfilListView.as_view(), name='listar_perfil'),
    #path('supplier/view/<int:pk>', views.supplier_view, name='supplier_view'),
    #path('supplier/new', views.supplier_create, name='supplier_new'),
    #path('supplier/edit/<int:pk>', views.supplier_update, name='supplier_edit'),
    #path('supplier/delete/<int:pk>', views.supplier_delete, name='supplier_delete'),
    path('gasto',  views.FilteredGastoListView.as_view(), name='listar_gasto'),
    #path('customer/view/<int:pk>', views.customer_view, name='customer_view'),
    #path('customer/new', views.customer_create, name='customer_new'),
    #path('customer/edit/<int:pk>', views.customer_update, name='customer_edit'),
    #path('customer/delete/<int:pk>', views.customer_delete, name='customer_delete'),
]