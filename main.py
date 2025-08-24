'''
    Arquivo principal do RAG que importa e executa as funções de crawler e parse
    Criado por: João Pedro de Sanches Pinheiro
'''
from sentence_transformers import SentenceTransformer

from crawler import extract_pdf_file
from parser import generate_dic
from rag import generate_embeddings, generate_answer, generate_text_answer, generate_llm_answer

# definicoes do iniciais para realizacao do scraping e parsing
START_URL = "https://scon.stj.jus.br/SCON/sumstj/"
PDF_FILE = "SumulasSTJ.pdf"
PATTERN_START = 'Excerto dos Precedentes Originários:'
PATTERN_END = 'Precedentes:'
LLM_MODEL = "gemini-1.5-flash"

if __name__=='__main__':

    prompt = input("Digite o prompt: ")
    print("\nGerando resposta... a primeira vez pode demorar um pouco mais...\n")
    texto = extract_pdf_file(START_URL, PDF_FILE)
    sumulas = generate_dic(texto, PATTERN_START, PATTERN_END)
    modelo = SentenceTransformer('all-mpnet-base-v2')
    sumulas_embeddings = generate_embeddings(sumulas, modelo)
    final_answer = generate_llm_answer(prompt, sumulas_embeddings, sumulas, modelo, LLM_MODEL)
    print(final_answer)