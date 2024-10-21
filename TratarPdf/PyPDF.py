import PyPDF2
import os 
import re

folder_path = "TratarPdf/PDF/"
# output_path = "fotos/editadas/"


# Caminho para o arquivo PDF
caminho_pdf = "teste01.pdf"

def OpenPDF(file_path):
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
                Identificador = line.replace("Identificador ","")
                
                Separe_identificador(Identificador)

        for line in text_complete.splitlines():
            if line.startswith("Inspeção"):
                inspecao = line.replace("Inspeção: ","")
                
                Separe_inspecao(inspecao)

                print(inspecao)

def Separe_identificador(Identificador):
    Poste = regex_Poste(Identificador)
    Parque = regex_Parque(Identificador)

    # print(f"{Parque} - {Poste}")
    ...

def Separe_inspecao(inspecao):
    Tipo = regex_Tipo(inspecao)
    print(f"Tipo: {Tipo}")

    # print(f"{Parque} - {Poste}")
    ...

def regex_Poste(Identificador):
    padrao = r"P\.[^ -]+"
    Poste = re.search(padrao, Identificador)
    return Poste.group(0) if Poste else None

    ...

def regex_Parque(Identificador):
    # Usar regex para remover tudo a partir de "P. ", incluindo "P." e o restante
    padrao = r"P\..*"
    texto_limpo = re.sub(padrao, "", Identificador).strip()
    
    # Remover espaços, hífens e zeros
    texto_limpo = re.sub(r"[ -]", "", texto_limpo)

    # Adicionar um espaço entre a parte alfabética e a numérica
    texto_com_espaco = re.sub(r"([A-Za-z])(\d+)", r"\1 \2", texto_limpo)
    
    # Formatar a parte numérica para ter dois dígitos
    texto_formatado = re.sub(r" (\d+)", lambda match: f" {int(match.group(1)):02}", texto_com_espaco)
    
    return texto_formatado

def regex_Tipo(inspecao):
    tipos_fichas = {
        "IMP": "Implantação",
        "FUN": "Fundação",
        "REP": "Reparo",
        "ESC": "Escavação",
    }

    # Cria um padrão de regex para buscar qualquer chave do dicionário
    pattern = re.compile("|".join(re.escape(key) for key in tipos_fichas.keys()))

    # Procura por uma correspondência na string e substitui pelo valor correspondente
    match = pattern.search(inspecao)

    if match:
        return tipos_fichas[match.group()]
    return inspecao  # Retorna a string original se nenhuma chave for encontrada
    ...




file_test = "TratarPdf/PDF/FormularioRealizado.pdf"


for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        file_path = os.path.join(folder_path,filename)
        
        if file_path == file_test:
            print(file_path)




