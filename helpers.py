import requests
from config import  URL_BASE_TOP_HEADLINES, URL_BASE_EVERYTHING, CHAVE_API

def top_noticias(pais, fonte=None, categoria=None, pesquisa=None):
    """
    retorna as top notícias do dia
    """
    if fonte:
        url = f"{URL_BASE_TOP_HEADLINES}sources={fonte}&apiKey={CHAVE_API}"
    elif categoria:
        url = f"{URL_BASE_TOP_HEADLINES}country={pais}&category={categoria}&apiKey={CHAVE_API}"
    elif pesquisa:
        url = f"{URL_BASE_TOP_HEADLINES}country={pais}&q={pesquisa}&apiKey={CHAVE_API}"
    else:
        url = f"{URL_BASE_TOP_HEADLINES}country={pais}&apiKey={CHAVE_API}"

    # Coletando dados em formato JSON
    resposta = requests.get(url).json()

    #pegando os artigos
    artigos = resposta["articles"]

    #criar lista vazia para pegar os detalhes das noticias
    lista_top_noticias = []

    for artigo in artigos:
        lista_top_noticias.append(f"{artigo['title']}, "
                              f"URL: {artigo['url']}, "
                              f"Publicado em: {artigo['publishedAt']}")

    return lista_top_noticias

def todas_noticias(pesquisa, lingua=None):
    """
    Retorna todas as notícias
    """

    if pesquisa:
        if lingua:
            url = f"{URL_BASE_EVERYTHING}q={pesquisa}&language={lingua}&apiKey={CHAVE_API}"

        resposta = requests.get(url).json()

        artigos = resposta["articles"]

        lista_noticias = []

        for artigo in artigos:
            lista_noticias.append(f"{artigo['title']}, "
                              f"URL: {artigo['url']}, "
                              f"Publicado em: {artigo['publishedAt']}")

        return lista_noticias
