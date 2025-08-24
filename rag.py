'''
    Arquivo que organiza as funções de RAG e Sentence Embedding usando a biblioteca
    sentence-transformers e seu modelo all-mpnet-base-v2
    Criado por: João Pedro de Sanches Pinheiro
'''

from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai
# from openai import OpenAI

GEMINI_KEY = 'INSERIR CHAVE DO GEMINI'

def generate_embeddings(dict, model):
    '''
        Argumentos:
            dict: dicionário no formato {inteiro: conteúdo} onde cada conteúdo
                  é um texto (no caso, as súmulas) que será gerado embeddings
            model: modelo de SentenceTransformer (semantico)
        Retorna:
            embeddings: dicionário no formato {inteiro: embeddings} onde cada
                        inteiro é o mesmo de dict e representa, nesse caso, o
                        número da súmula.
    '''

    modelo = model
    embeddings = {}
    for n, content in dict.items():
        embeddings[n] = modelo.encode(content)
    return embeddings


def generate_answer(prompt, embeddings_dict, content_dict, model):
    '''
        Argumentos:
            prompt: prompt entrada pelo usuário para realizar a busca pelos textos
                    mais relevantes por similaridade.
            embeddings_dict: dicionário com os vetores numericos das sumulas criado
                    a partir de generate_embeddings().
            content_dict: dicionário no formato {inteiro: conteúdo} onde cada 
                    conteúdo é um texto (no caso, as súmulas).
            model: modelo de SentenceTransformer (embeddings).
        Retorna:
            answer: string com as súmulas mais relevantes de acordo com a prompt
                    emitida pelo usuário
    '''
    modelo = model
    prompt_embedding = modelo.encode([prompt])[0].reshape(1, -1)
    indexes = list(embeddings_dict.keys())
    embeddings = np.array(list(embeddings_dict.values()))
    similarity = cosine_similarity(prompt_embedding, embeddings)[0]
    sorted_top = np.argsort(similarity)[::-1][:3]
    
    answer = 'Com base na prompt, as 3 súmulas mais relevantes encontradas foram: \n'
    for ind in sorted_top:
        real_ind = indexes[ind]
        simil_score = similarity[ind]
        answer += f'Sumula {real_ind} - similaridade: {simil_score:.2f}\n'
        answer += content_dict[real_ind] + '\n\n'
    
    return answer


def generate_text_answer(prompt, embeddings_dict, content_dict, model, gpt_model):
    '''
        Argumentos:
            prompt: prompt entrada pelo usuário para realizar a busca pelos textos
                    mais relevantes por similaridade.
            embeddings_dict: dicionário com os vetores numericos das sumulas criado
                    a partir de generate_embeddings().
            content_dict: dicionário no formato {inteiro: conteúdo} onde cada 
                    conteúdo é um texto (no caso, as súmulas).
            model: modelo de SentenceTransformer (embeddings).
        Retorna:
            answer: string com as súmulas mais relevantes de acordo com a prompt
                    emitida pelo usuário
    '''
    client = OpenAI(api_key=OPENAI_KEY)
    modelo = model
    prompt_embedding = modelo.encode([prompt])[0].reshape(1, -1)
    indexes = list(embeddings_dict.keys())
    embeddings = np.array(list(embeddings_dict.values()))
    similarity = cosine_similarity(prompt_embedding, embeddings)[0]
    top_match = np.argmax(similarity)

    context = f"""O usuário enviou o seguinte prompt {prompt}.
    
    O contexto mais relevante recuperado foi: 
    'Súmula {top_match + 1}: {content_dict[top_match + 1]}'

    Com base nessas informações, responda de forma clara se existe consonância.
    """
    
    answer = client.chat.completions.create(model=gpt_model,
                                            messages=[{"role": "system",
                                                       "content": "Você é um assistente jurídico que ajuda a verificar consonância entre ementas e súmulas."},
                                                       {"role": "user", 
                                                        "content": context}])
    return answer.choices[0].message.content

def generate_llm_answer(prompt, embeddings_dict, content_dict, model, llm_model):
    '''
        Argumentos:
            prompt: prompt entrada pelo usuário para realizar a busca pelos textos
                    mais relevantes por similaridade.
            embeddings_dict: dicionário com os vetores numericos das sumulas criado
                    a partir de generate_embeddings().
            content_dict: dicionário no formato {inteiro: conteúdo} onde cada 
                    conteúdo é um texto (no caso, as súmulas).
            model: modelo de SentenceTransformer (embeddings).
        Retorna:
            answer: string com as súmulas mais relevantes de acordo com a prompt
                    emitida pelo usuário
    '''
    genai.configure(api_key=GEMINI_KEY)
    generative_model = genai.GenerativeModel(llm_model)
    modelo = model
    prompt_embedding = modelo.encode([prompt])[0].reshape(1, -1)
    indexes = list(embeddings_dict.keys())
    embeddings = np.array(list(embeddings_dict.values()))
    similarity = cosine_similarity(prompt_embedding, embeddings)[0]
    top_match = np.argmax(similarity)

    context = f"""O usuário enviou o seguinte prompt {prompt}.
    
    O contexto mais relevante recuperado foi: 
    'Súmula {top_match + 1}: {content_dict[top_match + 1]}'

    Com base nessas informações, responda de forma clara se existe consonância.
    """
    
    answer = generative_model.generate_content(context)
    return answer.text
