# STJ_analisador_sumulas
(PT-BR)
Exemplo de Retrieval-Augmented Generation (RAG) aplicado a súmulas jurídicas do STJ, com Python e sentence-transformers, usando modelos LLM para gerar resposta textual. 

### Feito com

[![Python](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)](https://docs.python.org/3.10/)
[![Gemini](https://img.shields.io/badge/Django-000?style=for-the-badge&logo=gemini)](https://aistudio.google.com/welcome?utm_source=google&utm_medium=cpc&utm_campaign=FY25-global-DR-gsem-BKWS-1710442&utm_content=text-ad-none-any-DEV_c-CRE_726176647097-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt-Gemini-Gemini%20API%20Docs-KWID_43700081658555785-kwd-2327808654903&utm_term=KW_google%20gemini%20api%20documentation-ST_google%20gemini%20api%20documentation&gclsrc=aw.ds&gad_source=1&gad_campaignid=21026872772&gbraid=0AAAAACn9t67h14cfxXl8nzLIHXZH2jHrn&gclid=Cj0KCQjwzaXFBhDlARIsAFPv-u9il5RyEZ2XKWbM2RXEeaBLKLyy9_VRsk8CvpJ2dQohUB1cLMP-fNIaAlHnEALw_wcB)

### Instalação

(PT-BR)
* Faça o download dos arquivos um por um em um mesmo diretório ou clone o repositório utilizando o comando:
  >`git clone https://github.com/jotapesp/STJ-analisador-sumulas.git`

* Recomenda-se a criação de um ambiente virtual Python utilizando o venv
  > `python3 -m venv workplace`
  > `source workplace/bin/activate` para ativar o ambiente virtual em ambientes Linux e MacOS.
  > `workplace\Scripts\activate` para Windows

* Faça a instalação das dependências listadas em [`requirements.txt`](https://github.com/jotapesp/STJ-analisador-sumulas/blob/main/requirements.txt) manualmente ou utilize o comando:
  >`pip install -r requirements.txt`

* Para rodar o app, siga as instruções em Como Usar.

### Como usar

(PT-BR)
* O app foi feito utilizando o framework Django do Python, portanto, precisa-se seguir os seguintes passos para rodar o servidor local e a aplicação:
  * No terminal, vá até a pasta local do app onde está localizado um arquivo de nome `manage.py`
  * Na linha de comando do terminal, entre o comando:
    > `python3 manage.py runserver`

* Abra um navegador web de sua preferência e pela barra de endereços, acesse a URL: `http://127.0.0.1:8000/`.
* Na barra de URL encontrada na homepage, entre o URL pelo qual deseja iniciar o Web Crawling e clique em `Começar`.
* O processo de crawling se dará início e pode levar alguns minutos dependendo da quantidade de links encontrada.

### Web Crawling

* O processo de crawling e scraping é feito por uma API desenvolvida a parte localizada em `catalog/scraper.py`
* A documentação da API é encontrada [aqui](https://github.com/jotapesp/crawler_webapp/blob/main/API.md)
