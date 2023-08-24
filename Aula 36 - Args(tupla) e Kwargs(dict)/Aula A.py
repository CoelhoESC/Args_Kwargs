"""
Funções (def) - *args **kwargs
Tudo que entra no *args, sempre retorna em uma TUPLA!


Ex:
def func(a1, a2, a3, Nome=None, a5=None):  # À partir que foi dado um padrão ao parametro, os proximos teram que ter!
    print(a1, a2, a3, Nome, a5)


func(1, 2, 3, Nome='Everton', a5='Coelho')  # Quando for add padrão, tem que justificar o parametros!
"""


def func(*args, **kwargs):  # usa-se '*' para passar varios elementos!
    print(args)
    print(args[0])  # Posso acessar o elemento, usando index
    print(args[-1])
    print(len(args))
    args = list(args)  # Posso fazer test cast, convertendo á tupla em lista!
    args[0] = 20
    print(args)
    print(kwargs)  # Elementos que recebe nome (Dicionarios)


func(1, 2, 3, 4, 5, 6, nome='Everton', sobrenome='Coelho')

lista = [1, 2, 3, 4, 5, 6, 7]
print(*lista)  # Desempacotando uma lista


def retorne_tupla(*args):
    return args


print(retorne_tupla(lista))  # Retorna uma lista dentro da tupla!
