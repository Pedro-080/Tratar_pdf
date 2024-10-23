# def _criar_intervalos(dicionario):
#     # Obter as chaves e ordenar
#     # chaves = sorted(dicionario.keys())
#     # print(chaves)

#     # Criar o dicionário de intervalos
#     intervalos = {}
#     for i in range(len(chaves) - 1):
#         # O primeiro valor da tupla é a chave atual
#         # O segundo valor da tupla é a próxima chave - 1
#         intervalo = (chaves[i], chaves[i + 1] - 1)
#         # Adiciona ao dicionário, usando a chave atual
#         intervalos[chaves[i]] = intervalo
    
#     # Adiciona a última chave com um intervalo personalizado, se necessário
#     intervalos[chaves[-1]] = (chaves[-1], chaves[-1])
    
#     return intervalos



def _criar_intervalos(dicionario):
    # Obter as chaves e ordenar
    chaves = sorted(dicionario.keys())
    
    # Criar a lista de tuplas
    intervalos = {}
    for i in range(len(chaves) - 1):
        if i < len(chaves)-2:
            intervalo = (chaves[i], chaves[i + 1] - 1)
        else:
            intervalo = (chaves[i], chaves[i + 1])

        intervalos[chaves[i]] = intervalo

        # intervalos.append(intervalo)
    
    return intervalos



dados = {
0: 'A',
10: 'B',
20: 'C',
40: 'D',
60: 'C',
65: 'D',
}

resultado = _criar_intervalos(dados)
print(resultado[20])