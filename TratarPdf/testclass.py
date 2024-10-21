from Ficha import Ficha
import os 

folder_path = "TratarPdf/PDF/"
folder_limpos = "TratarPdf/PDF/Fichas"

caminho_pdf = "TratarPdf/PDF/SDP07 P.A18.02.pdf"

# ficha = Ficha(caminho_pdf)


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
        ficha = Ficha(file_path)
        # print(f"{ficha.parque} - {ficha.poste} - {ficha.tipo}")
        # print(f"{ficha.filepath}")
        ficha.renomear_pdf()



        # print(file_path)
