
def processar_whatsapp_message(lista, x=1, y=3, dados = []):
    """Processa os dados da mensagem buscando Dados Chave necessarios para os proximos
    passos da aplicação
    Recebe uma lista de String
    e a 
    posição inicial busca em X sendo o um item na lista 
    e posição y sendo a possição do dado requisitado pela aplicação
    dados é a lista com os dados requisitados para recurção"""
    entrada = lista[x].split('"')
    dados.append(entrada[y])
    if x == 21:
        processar_whatsapp_message(lista, x+(4*((x+5-(x//3))//3)), 1, dados)
    return dados
def is_valid_whatsapp_message(body, amostra) :
    return type(body) == type(amostra)