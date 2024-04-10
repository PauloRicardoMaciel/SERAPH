from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def testarEntrada(request):
    print(request.path)
    if request.method == "GET":
        recebido = request.GET
        print(recebido)
        return HttpResponse("Hello Word")
    if request.method == "POST":
        recebido = request.body
        body = recebido.decode("utf-8")
        lista = body.split(":")    
        print(lista)
        return HttpResponse(recebido)
def visaoTermo(request):
    render()
    
def visaoPolitica(request):
    render()
    