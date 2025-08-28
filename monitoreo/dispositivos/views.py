from django.shortcuts import render


def index(request):
    contexto = {"nombre": "Porfe Javier"}
    return render(request, "dispositivos/inicio.html", contexto)  
# Create your views here.
