from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from equipamentos import views  

urlpatterns = [
    path('visualizar-equipamentos/', views.visualizarEquipamentos, name='visualizar_equipamentos'), 
    path('', lambda request: redirect(views.visualizarEquipamentos, permanent=False)),
    path('admin/', admin.site.urls),
]
