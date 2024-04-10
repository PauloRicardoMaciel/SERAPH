import logging
from django.http import HttpRequest, HttpResponse
from Seraph import settings as current_app
from Seraph.sorce.processos import is_valid_whatsapp_message, processar_whatsapp_message
# from app.services.openai_service import generate_response
AMOSTRA = '''{
        "field": "messages",
        "value": {
        "messaging_product": "whatsapp",
        "metadata": {
        "display_phone_number": "16505551111",
        "phone_number_id": "123456123"
        }   ,
        "contacts": [
        {
        "profile": {
          "name": "test user name"
        },
        "wa_id": "16315551181"
        }
        ],
        "messages": [
        {
        "from": "16315551181",
        "id": "ABGGFlA5Fpa",
        "timestamp": "1504902988",
        "type": "text",
        "text": {
          "body": "this is a text message"
        }
        }
        ]
        }
        }'''

def lidar_message(request):
    """
    Lide com eventos de webhook recebidos da API do WhatsApp.

    Esta função processa mensagens recebidas do WhatsApp e outros eventos,
    como status de entrega. Se o evento for uma mensagem válida, ele será
    processado. Se a carga recebida não for um evento reconhecido do WhatsApp,
    um erro é retornado.

    Cada envio de mensagem irá acionar 4 solicitações HTTP para o seu webhook: mensagem, enviada, entregue, lida.

    Retorna:
        resposta: uma tupla contendo uma resposta JSON e um código de status HTTP.
    """
    body = request.body
    # logging.info(f"request body: {body}")
    body = body.decode("utf-8")
    dados = body.split(":")
    
    # Verifique se é uma atualização de status do WhatsApp
    # verifica se a mensagem é valida e processa a mesma 
    if is_valid_whatsapp_message(body,AMOSTRA.split(":")):
        processar_whatsapp_message(body)
    else:
        # Se a request não é um WhatsApp API event, return erro
        return (
            HttpResponse("404")
        )

# Requerimento de Verificação webhook para WhatsApp
def verify(request):
    
    recebido = request.GET
    return HttpResponse(recebido["hub.challenge"])



def webhook_get(request):
    return verify(request)


def webhook_post(request):
    return lidar_message(request)

def verificarMethod(request):
    if request.method == "GET":
        webhook_get(request)
    if request.method == "POST":
        webhook_post(request)