import PyPDF2
import os 
import re

folder_path = "TratarPdf/PDF/"
file_test = "TratarPdf/PDF/FormularioRealizado.pdf"


def OpenPDF(file_path):
    count=0
    Identificador = ""
    with open(file_path, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)
        text_complete = ""

        # Extraindo o texto de cada página
        for numb_pag, page in enumerate(pdf.pages):
            text = page.extract_text()
            text_complete += f"\n--- Página {numb_pag + 1} ---\n{text}"

        for line in text_complete.splitlines():
            if line.startswith("Identificador"):
                count+=1
                Identificador = line.replace("Identificador ","")
                print(f"Identificador: {count}")
                # Separe_identificador(Identificador)





for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        file_path = os.path.join(folder_path,filename)
        
        if file_path == file_test:
            OpenPDF(file_path)
            # print(file_path)

