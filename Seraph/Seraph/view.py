from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def testarEntrada(request):
        return HttpResponse("Hello Word")
    
def visaoTermo(request):
    render()
    
def visaoPolitica(request):
    render()
    