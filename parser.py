'''
    Código Python que recebe trata o texto raspado após um scraping a fim de 
    armazenar em um dicionario para futura comparação de conteúdo
    Criado por: João Pedro de Sanches Pinheiro
'''

def generate_dic(texto, pattern1, pattern2):
    '''
        Argumentos:
            texto: conteúdo bruto total do texto de pdf_name
            pattern1: substring de texto que será usada para identificar os índices
                      iniciais dos conteúdos iniciais que serão associadas a cada
                      key do dicionário.
            pattern2: substring de texto que será usara para identificar o índice 
                      final do conteúdo relevante de texto para ser associado com
                      cada key do dicionário.
        Retorna:
            sumulas: dicionário com as súmulas, onde cada key é um inteiro referente
                     a súmula e o conteúdo é o texto completo daquela súmula.
    '''
    indice_i = 0
    indice_f = 0

    sumulas = {}
    indice_sumula = 1

    while True:

        indice_i = texto.find(pattern1, indice_i)
        indice_f = texto.find(pattern2, indice_i)
        if indice_i == -1:
            break
        indice_i += len(pattern1)
        sumulas[indice_sumula] = texto[indice_i:indice_f]
        indice_i = indice_f + len(pattern2)
        indice_sumula += 1
    
    return sumulas



