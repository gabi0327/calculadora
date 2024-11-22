from django.urls import path
from. import views


urlpatterns = [
    # Otras rutas aquí...
  
    path('inicio/', views.inicio, name='inicio'),
    path('insertar_usuario/', views.insertar_usuario, name='insertar_usuario'),



 



]