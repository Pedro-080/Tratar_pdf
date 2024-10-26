class Pessoa:
    def __init__(self, nome):
        self.nome = nome  # Atributo 'nome'

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome  # Altera o atributo 'nome'

def atualizar_nomes(lista_pessoas, novo_nome):
    for pessoa in lista_pessoas:
        pessoa.alterar_nome(novo_nome)  # Chama o método da classe para alterar o atributo
    return lista_pessoas

# Criando instâncias da classe
pessoa1 = Pessoa("João")
pessoa2 = Pessoa("Maria")
pessoa3 = Pessoa("José")

# Lista de objetos Pessoa
lista_pessoas = [pessoa1, pessoa2, pessoa3]

# Atualizando o nome para "Carlos" em todas as instâncias
lista_atualizada = atualizar_nomes(lista_pessoas, "Carlos")

# Exibindo o nome atualizado de cada objeto
for pessoa in lista_atualizada:
    print(pessoa.nome)
