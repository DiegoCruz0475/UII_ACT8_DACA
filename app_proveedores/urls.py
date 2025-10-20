from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('editar/<int:id>/', views.editar_proveedor, name='editar_proveedor'),
    path('borrar/<int:id>/', views.borrar_proveedor, name='borrar_proveedor'),
]
