from helpers import top_noticias, todas_noticias

print("===COLETOR NOTÍCIAS VIA API - NEWSAPI.ORG===")
print()
print("Por favor, insira as informações solicitadas abaixo")
pais = input("Insira o país da notícia (br, us): ")
pesquisa = input("Insira o que pesquisar (palavra ou frase): ")
fonte = input("Insira a fonte (globo ou google-news-br): ")
categoria = input("Insira a categoria (business, general): ")

print()
print()
noticias = top_noticias(pais, pesquisa=pesquisa)

print(f"*** Listando as top notícias do País - {pais.upper()} ***")
if noticias:
    for numero in range(len(noticias)):
        print(f"{numero + 1} - {noticias[numero]}")
else:
    print("Não foi encontrada nenhuma notícia com essas opções")

print()
print()

td_noticias = todas_noticias(pesquisa=pesquisa, lingua='en')
print(f"*** Listando as notícias sobre - {pesquisa.upper()} ***")
if td_noticias:
    for numero in range(len(td_noticias)):
        print(f"{numero + 1} - {td_noticias[numero]}")
else:
    print("Não foi encontrada nenhuma notícia com essas opções")