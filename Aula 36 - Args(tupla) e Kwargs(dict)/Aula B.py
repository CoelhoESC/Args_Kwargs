"""
Função com **Kwargs -> retorna um dict, trabalha com keyword (chaves/momes)
"""


def func(**kwargs):
    nome = kwargs.get("nome")  # Verificando se existe a key nome!
    Sobrenome = kwargs.get("Sobrenome")
    idade = kwargs.get("idade")
    if idade or nome or Sobrenome is not None:
        print(nome, end=' ')
        print(Sobrenome, end=' ')
        print(idade)
    else:
        print('Nome, Sobrenome e idade nao existe')


func(nome='Everton', idade=22)


def dicionario(**kwargs):
    return kwargs


#                     chave  valor  (Tem que passar o nome da chave e depois o valor que a chave recebe)
variavel = dicionario(nome='Everton', sobrenome='Coelho', nome2='Fabio', sobrenome2='Silva')
for k, v in variavel.items():
    print(f'Meu {k} é {v}')
