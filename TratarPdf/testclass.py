from Ficha import Ficha
from Relatorio import Relatorio
import os 
import timeit

import tkinter as tk
from tkinter import filedialog, messagebox


folder_path = "TratarPdf/PDF/"

# folder_limpos = "TratarPdf/PDF/Fichas"

# caminho_pdf = "TratarPdf/PDF/SDP07 P.A18.02.pdf"

# ficha = Ficha(caminho_pdf)



# Código cuja execução deseja medir
def meu_codigo():
    for i in range(1000000):
        pass  # Substitua pelo seu código


# print(f"{ficha.filepath}")
# print(f"{os.path.dirname(ficha.filepath)}")
# ficha.ReadPDF()
# ficha.renomear_pdf()


# print(f"Parque: {ficha.parque}")
# print(f"Poste: {ficha.poste}")
# print(f"Tipo: {ficha.tipo}")


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


# for filename in os.listdir(folder_path):
#     if filename.endswith(".pdf"):
#         file_path = os.path.join(folder_path,filename)
#         relatorio = Relatorio(file_path)

        



if __name__ == "__main__":
    lista_relatorios = selecionar_fonte()
    arquivo_destino = selecionar_destino()
    # print(f"arquivos: {type(arquivos)}")

    # print(f"destino: {arquivo_destino}")



    for arquivo in lista_relatorios:
        relatorio = Relatorio(arquivo)
        relatorio.Salvar_Relatorio(arquivo_destino)
        # relatorio.test()

        # for item in relatorio.lista_de_fichas:
        #     print(item)

        # print(f"tipo: {type(relatorio.lista_de_fichas)}")
        # print(f"tipo: {type(relatorio.lista_de_fichas)}")

        # print(f"arquivos: {arquivo}")
        ...

    # print(f"arquivos: {arquivo}")



# Medindo o tempo total de execução
tempo_total = timeit.timeit(meu_codigo, number=1)
print(f"Tempo total de execução: {tempo_total:.4f} segundos")