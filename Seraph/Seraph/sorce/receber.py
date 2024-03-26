import logging
from django.http import HttpRequest
from Seraph import settings as current_app

# from app.services.openai_service import generate_response

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
    body = request.GET
    # logging.info(f"request body: {body}")

    # Check if it's a WhatsApp status update
    if (
        body.get("entry", [{}])[0]
        .get("changes", [{}])[0]
        .get("value", {})
        .get("statuses")
    ):
        logging.info("Received a WhatsApp status update.")
        # return jsonify({"status": "ok"}), 200

    try:
        if is_valid_whatsapp_message(body):
            process_whatsapp_message(body)
            # return jsonify({"status": "ok"}), 200
        else:
            # if the request is not a WhatsApp API event, return an error
            return (
                jsonify({"status": "error", "message": "Not a WhatsApp API event"}),
                404,
            )
    except json.JSONDecodeError:
        logging.error("Failed to decode JSON")
       # return jsonify({"status": "error", "message": "Invalid JSON provided"}), 400


# Required webhook verifictaion for WhatsApp
def verify(request):
    # Parse params from the webhook verification request
    mode = request.GET("hub.mode")
    token = request.GET("hub.verify_token")
    challenge = request.GET("hub.challenge")
    # Check if a token and mode were sent
    if mode and token:
        # Check the mode and token sent are correct
        if mode == "subscribe" and token == current_app.config["VERIFY_TOKEN"]:
            # Respond with 200 OK and challenge token from the request
            logging.info("WEBHOOK_VERIFIED")
            return challenge, 200
        else:
            # Responds with '403 Forbidden' if verify tokens do not match
            logging.info("VERIFICATION_FAILED")
            # return jsonify({"status": "error", "message": "Verification failed"}), 403
    else:
        # Responds with '400 Bad Request' if verify tokens do not match
        logging.info("MISSING_PARAMETER")
        # return jsonify({"status": "error", "message": "Missing parameters"}), 400



def webhook_get(request):
    return verify(request)


def webhook_post(request):
    return lidar_message(request)

def verificarMethod(request):
    if request.method == "GET":
        webhook_get(request)
    if request.method == "POST":
        webhook_post(request)