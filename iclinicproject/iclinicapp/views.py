from django.shortcuts import render
import requests



def pagina_inicial(request):
    return render(request, 'index.html')
