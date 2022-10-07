from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
# Navegar até o whatsapp web

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)

# Definir contatos e grupos e mensagem a ser enviada
contatos = ['Estudos Programação', 'Amor']
mensagem = 'Teste automação Python'
# Buscar contatos


def buscar_contato(contato):
    campo_pesquisa = driver.find_element(By.CLASS_NAME, 'copyable-text selectable-text')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)


def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements(By.XPATH,
        '//div[contains(@class,"selectable-text copyable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)



for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
