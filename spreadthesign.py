import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import unicodedata
import pandas as pd
import csv

'''
DÚVIDAS:

*** Como fazer ele percorrer todos os topicos e SUBTÓPICOS?
- Fazer manualmente?
- Passando como:
    urls_paginas = [('https://www.spreadthesign.com/pt.br/search/by-category/', 100)]
 alguns links são invalidos.

 *** Como normalizar os caracteres corretamente? 
- Pedi ajuda para o chat gpt que me indicou a biblioteca unicodedata
- Mass alguns acentos são perdidos
 
urls_paginas = [
    ('https://www.spreadthesign.com/pt.br/search/by-category/398/lingua-de-sinais-para-iniciantes/?q=&p=', 6),
    ('https://www.spreadthesign.com/pt.br/search/by-category/1/diversos/?q=&p=', 23),
    ('https://www.spreadthesign.com/pt.br/search/by-category/37/frases/?q=&p=', 2),
    ('https://www.spreadthesign.com/pt.br/search/by-category/86/religiao/?q=&p=', 9),
    ('https://www.spreadthesign.com/pt.br/search/by-category/13/pedagogia/?q=&p=', 15),
    ('https://www.spreadthesign.com/pt.br/search/by-category/13/pedagogia/?q=&p=', 15),
    ('https://www.spreadthesign.com/pt.br/search/by-category/28/lingua/?q=&p=', 62),
    ('https://www.spreadthesign.com/pt.br/search/by-category/113/arte-e-entretenimento/?q=&p=', 28),
    ('https://www.spreadthesign.com/pt.br/search/by-category/46/estudos-sociais/?q=&p=', 55)
    (),
    # Link, numero de pags
]

urls_paginas = [('https://www.spreadthesign.com/pt.br/search/by-category/', 100)]
'''

urls_paginas = [
    ('https://www.spreadthesign.com/pt.br/search/by-category/398/lingua-de-sinais-para-iniciantes/?q=&p=', 1)]


def gerar_vetor_urls(urls_paginas):
    urls = []

    for url, num_pages in urls_paginas:
        for page in range(1, num_pages + 1):
            url_pagina = url + str(page)
            urls.append(url_pagina)

    return urls

#ooooi

def obter_videos_site(urls):
    options = Options()
    options.headless = True #Ativado para que navegador não abra.

    driver = webdriver.Chrome(options=options)

    lista_videos = []

    for url in urls:

        driver.get(url)

        time.sleep(5)  # delay para carregar a página

        html = driver.page_source  # pega o html
        soup = BeautifulSoup(html, 'html.parser')  # organiza

        # Encontrar todas as divs com a classe search-result-title (onde estão as palavras)
        divs = soup.find_all('div', class_='search-result-title')

        for div in divs:
            atags = div.find_all('a')  # atags = todos os "a"

            for a in atags:
                # Excluir a tag <small> do conteúdo de cada "a", pois não queremos "substantivo", "verbo", etc
                small_tag = a.find('small')
                if small_tag:
                    small_tag.decompose()

                # Extrair o texto do elemento 'a'
                text = a.get_text(strip=True) 
                # strip=True remove espaços em branco extras no início e no final do texto.

                # Remover caracteres de controle e normalizar os caracteres Unidecode (Feito pelo ChatGPT)
                text = "".join(ch for ch in text if unicodedata.category(ch)[0] != "C")
                text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')

                # Obter o link do elemento 'a'
                href = a['href']

                # Abrir o link em uma nova aba
                driver.execute_script("window.open(arguments[0], '_blank');", href)
                time.sleep(1)  # Aguardar um segundo após o clique

                # Alternar para a nova aba
                driver.switch_to.window(driver.window_handles[-1])

                # Obter o HTML da nova página
                video_html = driver.page_source
                video_soup = BeautifulSoup(video_html, 'html.parser')

                # Encontrar a div que contém o vídeo
                video_div = video_soup.find('div', class_='col-md-7')

                if video_div:
                    # Verificar se há um elemento de vídeo presente
                    video_tag = video_div.find('video')
                    if video_tag:
                        # Obter o valor do atributo 'src' do vídeo
                        video_src = video_tag.get('src')
                        lista_videos.append((text, video_src))
                    else:
                        lista_videos.append((text, 'null'))
                else:
                    lista_videos.append((text, 'null'))

                # Fechar a nova aba e voltar para a aba anterior
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

    driver.quit()
    df_videos = pd.DataFrame(lista_videos, columns=['Palavra', 'Link'])
    df_videos['Instituicao'] = 'Spread the Sign' 

    return df_videos

urls = gerar_vetor_urls(urls_paginas)
print(urls)

df_videos = obter_videos_site(urls)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
print(df_videos)

# Salvar DataFrame em um arquivo CSV
nome_arquivo = 'spreadthesign.csv'
formato = {
    'Palavra': str,
    'Link': str,
    'Instituicao': str
}
with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.DictWriter(arquivo_csv, fieldnames=formato.keys())
    escritor.writeheader()
    for _, linha in df_videos.iterrows():
        escritor.writerow({campo: formato[campo](valor) for campo, valor in linha.items()})

print("Dados salvos em arquivo CSV:", nome_arquivo)