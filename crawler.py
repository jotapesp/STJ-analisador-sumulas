'''
    Conteúdo do Crawler e Scraper.
    Funções para realizar crawling em páginas Web e obter seu código
    HTML completo ou conteúdo em tags específicas.
    Criado por: João Pedro de Sanches Pinheiro
'''

from bs4 import BeautifulSoup # type: ignore
from urllib.parse import urljoin, urlparse # manipulacao dos URLs durante o scraping
import requests # biblioteca para realizar os requests aos URLs
import os
from io import BytesIO # manipular PDF direto da memoria como arquivo
import fitz # PyMuPDF para manipular PDFs

def get_page_content(URL):
    '''
        Argumentos:
            URL: string que representa o endereço de uma página na Web
        Retorna:
            html_content: conteúdo HTML de URL em formato BeautifulSoup da
                          biblioteca bs4
    '''
    response = requests.get(URL)
    html_content = BeautifulSoup(response.text, 'html.parser')

    return html_content

def put_url_together(base_url, attach_urls):
    '''
    Argumentos:
        base_url: string contendo o URL "crawled" originalmente
        attach_urls: lista de strings com todos os URLs que se deseja
                     juntar ao URL da home page a fim de criar-se URLs
                     completos.
    Retorno:
        full_addresses: lista de strings com os endereços finais completos
                        considerando-se o URL original e sua home page.
    '''
    start_address = f'{urlparse(base_url).scheme}://{urlparse(base_url).netloc}'
    full_addresses = []
    for url in attach_urls:
        s = url
        if not url.startswith('https'):
            s = start_address + url
        full_addresses.append(s)
    return full_addresses

def extract_pdf_file(URL, pdf_name):

    '''
    Extrai o arquivo PDF especificado por pdf_name de um URL.
    Funciona como um Scraper.
    Argumentos:
        URL: endereço URL de onde o PDF será extraído
        pdf_name: string com o nome do PDF específico
    Retorna:
        file_text: string com todo o conteúdo de texto de pdf_name
    '''

    a = get_page_content(URL)
    sections = a.find_all('a')
    ls = []
    for item in sections:
        if 'href' in item.attrs:
            ls.append(item['href'])

    urls = put_url_together(URL, ls)

    target_url = ''
    for url in urls:
        if url.endswith(pdf_name):
            target_url = url

    response = requests.get(target_url)
    pdf = BytesIO(response.content)

    pdf_doc = fitz.open(stream=pdf, filetype='pdf')

    file_text = ''
    for page in pdf_doc:
        file_text += page.get_text("text") + "\n"

    return file_text
