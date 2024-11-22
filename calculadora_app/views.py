# Create your views here.
from django.shortcuts import render






def inicio(request):
    return render(request,'inicio.html')




def insertar_usuario(request):
    return render(request,'insertar_usuario.html')