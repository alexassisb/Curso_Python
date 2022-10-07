#importar bibliotecas necessárias
import pywhatkit
import keyboard
import time
from datetime import datetime

#definir para quais contatos enviar as mensagens

contatos = ['+5535988777407', '+5535988038615']

while len(contatos) >=1:
    #enviar mensagem 
    pywhatkit.sendwhatmsg(contatos[0],'Bot:Teste de automação com Python',
datetime.now().hour, datetime.now().minute + 1)
del contatos[0]
time.sleep(15)
keyboard.press_and_release('crtl+w')
    