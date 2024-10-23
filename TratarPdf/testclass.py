from Ficha import Ficha
from Relatorio import Relatorio
import os 
import timeit

folder_path = "TratarPdf/PDF/"
folder_limpos = "TratarPdf/PDF/Fichas"

caminho_pdf = "TratarPdf/PDF/SDP07 P.A18.02.pdf"

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







for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        file_path = os.path.join(folder_path,filename)

        relatorio = Relatorio(file_path)
        

        # ficha = Ficha(file_path)





        # print(f"{ficha.parque} - {ficha.poste} - {ficha.tipo}")
        # print(f"{ficha.filepath}")
        # ficha.renomear_pdf()




        # print(file_path)

        
# Medindo o tempo total de execução
tempo_total = timeit.timeit(meu_codigo, number=1)
print(f"Tempo total de execução: {tempo_total:.4f} segundos")