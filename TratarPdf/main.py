# from Ficha import Ficha
from Relatorio import Relatorio
import os 
import timeit

import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd


# Código cuja execução deseja medir
def meu_codigo():
    for i in range(1000000):
        pass  # Substitua pelo seu código

def selecionar_fonte():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    arquivos_origem = filedialog.askopenfilenames(title="Selecione os arquivos para copiar")
    return arquivos_origem

def selecionar_destino():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    destino = filedialog.askdirectory(title="Selecione o diretório de destino")
    return destino
     

def Criar_Excel(dataframes, save_path):
    nome_arquivo = save_path + '/Tabela_resumo.xlsx'

    df = pd.concat(dataframes, ignore_index=True)

    # print(df)


    # Exportando para um arquivo Excel
    df.to_excel(nome_arquivo, index=False)


    # print(df)aminho_arquivo)

    # print(f"Aqui: {}")

#     ...


dataframes = []

if __name__ == "__main__":
    lista_relatorios = selecionar_fonte()
    arquivo_destino = selecionar_destino()

    for arquivo in lista_relatorios:
        relatorio = Relatorio(arquivo)
        dataframes.append(relatorio.Salvar_Relatorio(arquivo_destino))
        
        
        # Criar_excel(relatorio.lista_de_fichas,arquivo_destino,arquivo)

    Criar_Excel(dataframes, arquivo_destino)

    # for df in dataframes:
    #     print(df)




# Medindo o tempo total de execução
tempo_total = timeit.timeit(meu_codigo, number=1)
print(f"Tempo total de execução: {tempo_total:.4f} segundos")