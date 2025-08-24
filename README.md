# STJ_analisador_sumulas
(PT-BR)
Exemplo de Retrieval-Augmented Generation (RAG) aplicado a súmulas jurídicas do STJ, com Python e sentence-transformers, usando modelos LLM para gerar resposta textual. 
O programa foi desenvolvido para realizar o scraping do endereço oficial do STJ: `https://scon.stj.jus.br/SCON/sumstj/`, a fim de encontrar e analisar o
arquivo PDF que contém as súmulas a serem analisadas.

### Feito com

[![Python](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)](https://docs.python.org/3.10/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-886FBF?logo=googlegemini&logoColor=fff)](https://aistudio.google.com/welcome?utm_source=google&utm_medium=cpc&utm_campaign=FY25-global-DR-gsem-BKWS-1710442&utm_content=text-ad-none-any-DEV_c-CRE_726176647097-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt-Gemini-Gemini%20API%20Docs-KWID_43700081658555785-kwd-2327808654903&utm_term=KW_google%20gemini%20api%20documentation-ST_google%20gemini%20api%20documentation&gclsrc=aw.ds&gad_source=1&gad_campaignid=21026872772&gbraid=0AAAAACn9t67h14cfxXl8nzLIHXZH2jHrn&gclid=Cj0KCQjwzaXFBhDlARIsAFPv-u9il5RyEZ2XKWbM2RXEeaBLKLyy9_VRsk8CvpJ2dQohUB1cLMP-fNIaAlHnEALw_wcB)

#### Desenvolvido em Ubuntu 24.04.5 utilizando **Python 3.10.12**, portanto, pode haver incompatibilidades ao tentar instalar as bibliotecas das dependências

### Instalação

(PT-BR)
* Faça o download dos arquivos um por um em um mesmo diretório ou clone o repositório utilizando o comando:
  >`git clone https://github.com/jotapesp/STJ-analisador-sumulas.git`

* Recomenda-se a criação de um ambiente virtual Python utilizando o venv
  > `python3 -m venv workplace` ;
  > `source workplace/bin/activate` para ativar o ambiente virtual em ambientes Linux e MacOS.
  > `workplace\Scripts\activate` para Windows

* Faça a instalação das dependências listadas em [`requirements.txt`](https://github.com/jotapesp/STJ-analisador-sumulas/blob/main/requirements.txt) manualmente ou utilize o comando:
  >`pip install -r requirements.txt`

* Para rodar o app, siga as instruções em Como Usar.

### Como usar

(PT-BR)
* O programa principal é o `main.py`, que está configurado para rodar o modelo LLM do Google Gemini, que requere uma key. Para inserir a key:
  1. Abra `rag.py` no editor de texto
  2. Altere o campo `GEMINI_KEY = 'INSERIR CHAVE DO GEMINI'` inserindo a chave do Gemini entre aspas.
* Para rodar:
  * No terminal, vá até a pasta local do app onde está localizado um arquivo de nome `main.py`
  * Na linha de comando do terminal, rode o programa utilizando o script:
    > `python3 main.py`
  * Entre a prompt quando for solicitado.
  * Aguarde a resposta gerada aparecer na tela.

