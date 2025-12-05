import tkinter as tk
from tkinter import filedialog
import PyPDF2
import os
import re


# Criar a janela de seleção de arquivo
root = tk.Tk()
root.withdraw()  # Esconde a janela principal

def extrair_texto_pdf(caminho_pdf):
    """Extrai o texto de um arquivo PDF e filtra as linhas com '70mm'."""
    with open(caminho_pdf, "rb") as arquivo:
        leitor = PyPDF2.PdfReader(arquivo)
        texto = ""
        for pagina in range(len(leitor.pages)):
            texto += leitor.pages[pagina].extract_text() + "\n"
        
        # Filtra as linhas com "70mm"
        texto_70mm = filtrar_linhas_com_70mm(texto)
        return texto_70mm

def filtrar_linhas_com_70mm(texto):
    """Filtra e retorna apenas as linhas que contêm '70mm' após 'P.' até encontrar 'Ω'."""
    linhas = texto.split("\n")
    linhas_filtradas = []

    for linha in linhas:
        if "70mm" in linha:
            # Encontrar a posição de "P." e pegar o texto a partir daí
            posicao_p = linha.find("P.")
            if posicao_p != -1:  # Se "P." for encontrado
                # Cortar a linha até o caractere "Ω" (se encontrado)
                posicao_omega = linha.find("Ω", posicao_p)
                if posicao_omega != -1:
                    linha = linha[posicao_p:posicao_omega+1]  # Inclui o "Ω"
                else:
                    linha = linha[posicao_p:]  # Caso não tenha "Ω", mantém o texto a partir de "P."
                
                # Substitui "70mm² NA " por " - "
                linha = linha.replace("70mm² NA ", " - ")

                linhas_filtradas.append(linha)  # Adiciona a linha processada à lista
    
    return linhas_filtradas

def extrair_Parque(file_path):
    """Extrai o trecho 'SDP __' do nome do arquivo PDF."""
    file_name = os.path.basename(file_path)
    file_name = file_name.replace(" ", "").replace(".pdf", "")  # Remove espaços e ".pdf"
    
    match = re.search(r"SDP(\d{2})", file_name)  # Espera dois dígitos numéricos após "SDP"
    if match:
        return f"SDP {match.group(1)}"  # Retorna "SDP 01", "SDP 02", etc.
    return None  # Retorna None caso não encontre

# Selecionar múltiplos arquivos PDF
file_paths = filedialog.askopenfilenames(title="Selecione um ou mais arquivos PDF", filetypes=[("Arquivos PDF", "*.pdf")])

# Iterar sobre os arquivos selecionados
for file_path in file_paths:
    Parque = extrair_Parque(file_path)  # Extrai o Parque do nome do arquivo

    # Extrai o texto e filtra as linhas com "70mm"
    texto_70mm = extrair_texto_pdf(file_path)
    
    if texto_70mm:
        for linha in texto_70mm:
            print(f"{Parque} - {linha}")  # Imprime o Parque seguido da linha filtrada
    else:
        print(f"{Parque} - Nenhuma linha com '70mm' encontrada.")
