import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unidecode
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

'''
Melhorias que ainda serão realizadas:
- transformar em funcao
- alguns links nao foram coletados corretamente com essa alternativa, entao vamos voltar para
a alternativa 1 de cliclar atraves do selenium e coletar links.

'''

driver.get('http://www.acessibilidadebrasil.org.br/libras_3/')

time.sleep(5)

letras_menu = driver.find_elements(By.XPATH, '//div[@id="filter-letter"]/ul/li/a')

lista_option_texts = []
links_videos = []

for letra in letras_menu:
    letra.click()  
    
    time.sleep(1)  

    html = driver.page_source 
    soup = BeautifulSoup(html, 'html.parser')

    options = soup.find_all('option')[1:]
    
    for option in options:
        option_text = option.text
        option_text = option_text.lower()  
        option_text = unidecode.unidecode(option_text)
        option_text = option_text.replace(" ", "_") 
        lista_option_texts.append(option_text)

for texto in lista_option_texts:
    url = "http://www.acessibilidadebrasil.org.br/libras_3/public/media/palavras/videos/" + texto + "Sm_Prog001.mp4"
    time.sleep(0.4)
    # Verifica se a página contém a mensagem de erro
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    error_message = soup.find(text="Desculpe, mas aconteceu um erro.")

    if error_message:
        print(f"A página {url} apresenta a mensagem de erro.")
    else:
        links_videos.append(url)

print(links_videos)

driver.quit()

'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unidecode
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

driver.get('http://www.acessibilidadebrasil.org.br/libras_3/')

letras_menu = driver.find_elements(By.XPATH, '//div[@id="filter-letter"]/ul/li/a')

lista_option_texts = []
links_videos = []

for letra in letras_menu:
    letra.click()

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    options = soup.find_all('option')[1:]

    for option in options:
        option_style = option.get('style')
        if option and not option_style or 'display: none' not in option_style:  # Verifica se o objeto option existe e está visível
            option_text = option.text
            option_text = option_text.lower()
            option_text = unidecode.unidecode(option_text)
            option_text = option_text.replace(" ", "_")
            lista_option_texts.append(option_text)

for texto in lista_option_texts:
    url = "http://www.acessibilidadebrasil.org.br/libras_3/public/media/palavras/videos/" + texto + "Sm_Prog001.mp4"
    time.sleep(0.4)
    # Verifica se a página contém a mensagem de erro
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    error_message = soup.find(text="Desculpe, mas aconteceu um erro.")

    if error_message:
        print(f"A página {url} apresenta a mensagem de erro.")
    else:
        links_videos.append(url)

print(links_videos)

driver.quit()

'''
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unidecode
from bs4 import BeautifulSoup

driver = webdriver.Chrome()


Melhorias que ainda serão realizadas:
- transformar em funcao
- alguns links nao foram coletados corretamente com essa alternativa, entao vamos voltar para
a alternativa 1 de cliclar atraves do selenium e coletar links.



driver.get('http://www.acessibilidadebrasil.org.br/libras_3/')

time.sleep(5)

letras_menu = driver.find_elements(By.XPATH, '//div[@id="filter-letter"]/ul/li/a')

lista_option_texts = []
links_videos = []

for letra in letras_menu:
    letra.click()  
    
    time.sleep(1)  

    html = driver.page_source 
    soup = BeautifulSoup(html, 'html.parser')

    options = soup.find_all('option')[1:]
    
    for option in options:
        option_text = option.text
        option_text = option_text.lower()  
        option_text = unidecode.unidecode(option_text)
        option_text = option_text.replace(" ", "_") 
        lista_option_texts.append(option_text)

for texto in lista_option_texts:
    links_videos.append("http://www.acessibilidadebrasil.org.br/libras_3/public/media/palavras/videos/" + texto + "Sm_Prog001.mp4")

print(links_videos)

driver.quit()
'''
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unidecode
from bs4 import BeautifulSoup

# Inicialize o driver do Selenium
driver = webdriver.Chrome()

# Abra a página inicial
driver.get('http://www.acessibilidadebrasil.org.br/libras_3/')

time.sleep(5)  # Aguarde um tempo para a página ser carregada

# Encontre a lista de letras do menu
letras_menu = driver.find_elements(By.XPATH, '//div[@id="filter-letter"]/ul/li/a')

lista_option_texts = []
links_videos = []

# Percorra cada letra no menu
for letra in letras_menu:
    letra.click()  
    time.sleep(1)  

    html = driver.page_source 
    soup = BeautifulSoup(html, 'html.parser')

    options = soup.find_all('option')[1:]
    
    for option in options:
        option_text = option.text
        lista_option_texts.append(option_text)

for text in lista_option_texts:
    link_text = text.lower() 
    link_text = unidecode.unidecode(link_text)  
    link_text = option_text.replace(" ", "_")  
    lista_option_texts.append(link_text)

    links_videos.append("http://www.acessibilidadebrasil.org.br/libras_3/public/media/palavras/videos/" + link_text + "Sm_Prog001.mp4")

print(links_videos)



driver.quit()


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unidecode

# Inicialize o driver do Selenium
driver = webdriver.Chrome()

# Abra a página inicial
driver.get('http://www.acessibilidadebrasil.org.br/libras_3/')

time.sleep(5)  

# Encontre a lista de letras do menu
letras_menu = driver.find_elements(By.XPATH, '//div[@id="filter-letter"]/ul/li/a')

lista_option_texts = []
links_videos = []

for letra in letras_menu:
    letra.click()  
    
    time.sleep(1)
    
    select_element = Select(driver.find_element(By.ID, 'input-palavras'))
    
    options = select_element.options
    
    for option in options:
        option.click()  # Clique na opção
        time.sleep(1)  # Aguarde um tempo para a página da palavra ser carregada
        option_text = option.text
        lista_option_texts.append(option_text)

    # Volte para a página inicial
    driver.get('http://www.acessibilidadebrasil.org.br/libras_3/')
    time.sleep(1)  # Aguarde um tempo para a página inicial ser carregada novamente

for texto in lista_option_texts:
    texto = texto.lower()  # Converte o texto para minúsculas
    texto = unidecode(texto)
    links_videos.append("http://www.acessibilidadebrasil.org.br/libras_3/public/media/palavras/videos/"+texto+"Sm_Prog001.mp4")

driver.quit()


'''

'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup

# Inicialize o driver do Selenium
driver = webdriver.Chrome()

# Abra a página com o menu
driver.get('http://www.acessibilidadebrasil.org.br/libras_3/')

# Encontre a lista de itens do menu pelo ID
menu_items = driver.find_elements(By.XPATH, '//div[@id="filter-letter"]/ul/li/a')

options_list = []
options_values = []

# Percorra cada item do menu e clique nele
for item in menu_items:

    item.click()  # Clique no item para revelar as opções
    time.sleep(1)
    options = item.find_elements(by=By.TAG_NAME, value='option')
    options_list.extend(options)
    
print(options_list)
driver.quit()

html = driver.page_source  # pega o html
    soup = BeautifulSoup(html, 'html.parser')

    options = soup.find_all('option')

    print(options)
'''

