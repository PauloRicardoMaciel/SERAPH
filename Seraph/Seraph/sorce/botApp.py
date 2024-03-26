import webbrowser
from urllib.parse import quote
import time 
import os
import pyautogui

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Olá Mundo Sou Seraph"
        
    def enviarMensagens(self):
        telefone = 5547999282154
        link =f'https://web.whatsapp.com/send?phone={telefone}&text={quote(self.mensagem)}'
        webbrowser.open(link)
        time.sleep(10)
        seta = pyautogui.locateCenterOnScreen('seta.png')
        time.sleep(5)
        pyautogui.click(seta[0], seta[1])
        time.sleep(5)
        self.desconectar()
        
    def conectar(self):
        webbrowser.open("https://web.whatsapp.com")
        time.sleep(30)
        self.desconectar()
        self.enviarMensagens()
        
    def desconectar(self):
        pyautogui.hotkey("ctrl","w")
        time.sleep(5)


if __name__ == "__main__":
    bot = WhatsappBot()
    bot.conectar()