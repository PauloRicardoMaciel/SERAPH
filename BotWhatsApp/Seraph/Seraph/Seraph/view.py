from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def testarEntrada(request):
    print(request.path)
    if request.method == "GET":
        recebido = request.GET
        print(recebido)
        return HttpResponse("Teste Entrada", recebido)
    if request.method == "POST":
        recebido = request.POST
        print(recebido)
        return HttpResponse("Teste Entrada", request.POST)