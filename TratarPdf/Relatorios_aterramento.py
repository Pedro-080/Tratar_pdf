import tkinter as tk
from tkinter import filedialog
import PyPDF2
import os
import re


def extrair_texto_pdf(caminho_pdf):
    """Extrai o texto de um arquivo PDF e filtra as linhas com '70mm'."""
    with open(caminho_pdf, "rb") as arquivo:
        leitor = PyPDF2.PdfReader(arquivo)
        texto = ""
        for pagina in range(len(leitor.pages)):
            texto += leitor.pages[pagina].extract_text() + "\n"

        return texto

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


# def extrair_Poste(texto):
#     """Filtra e retorna apenas as linhas que contêm '70mm' após 'P.' até encontrar 'Ω'."""
#     linhas = texto.split("\n")
#     linhas_filtradas = []

#     for linha in linhas:
#         if " NA " in linha:
#             match = re.search(r'(P[^\s]+)', linha)
#             linhas_filtradas.append(match.group(1) if match else None)

    
#     return linhas_filtradas


def extrair_Poste_e_resistencia(texto):
    """Filtra e retorna apenas as linhas que contêm '70mm' após 'P.' até encontrar 'Ω'."""
    linhas = texto.split("\n")
    linhas_filtradas = []

    for linha in linhas:
        if " NA " in linha:
            # print(linha)
            match_Poste = re.search(r"(?:P\.|PA)([^\s]*)", linha)
            Poste = match_Poste.group(0) if match_Poste else None
            
            

            match_resis = re.search(r'(\S+)\s*Ω', linha)
            Resistencia = match_resis.group(1) if match_resis else None
            Resistencia = Resistencia.replace(".",",")
            # print(Resistencia)

            linhas_filtradas.append(f"{Poste} - {Resistencia}")

            # print(match_resis.group(1) if match_resis else None)

            
            
    
    return linhas_filtradas




def extrair_temperatura(texto):
    linhas = texto.split("\n")
    linhas_filtradas = []

    for linha in linhas:
        if " GROUD " in linha:
            # print(linha)
            # match = re.search(r"Temperatura:\s*(-?\d+,\d+)", texto)
            match = re.search(r"Temperatura:\s*(-?\d+,\d+)", texto)
            Temperatura = match.group(1) if match else None
            
            if match == None:
                match = re.search(r'Temperatura:\s*([\d,\.]+)\s*º', linha)
                 

            Temperatura = match.group(1)

            # print(Temperatura)
            linhas_filtradas.append(Temperatura)  # Adiciona a linha processada à lista

    return linhas_filtradas



def extrair_Umidade_old(texto):
    linhas = texto.split("\n")
    linhas_filtradas = []

    for linha in linhas:
        if "00119907"  in linha or "4396795" in linha:
            # print(linha)
            match_umidade= re.search(r'Umidade \s*([\d,\.]+)\s*%', linha)
            Umidade = match_umidade.group(1) if match_umidade else None
            # print(Temperatura)

            linhas_filtradas.append(Umidade)  # Adiciona a linha processada à lista

    return linhas_filtradas

def extrair_Umidade(texto,arquivo):
    linhas = texto.split("\n")
    linhas_filtradas = []

    for linha in linhas:
        # print(linha)
        if "%"  in linha and "º" not in linha:
        # if "%"  in linha:  
            # print(linha)
            match_umidade= re.search(r'(\S+)%', linha)
            Umidade = match_umidade.group(0) if match_umidade else None
            # print(f"{arquivo} - {Umidade}")

            linhas_filtradas.append(Umidade)  # Adiciona a linha processada à lista

    return linhas_filtradas

def extrair_Parque(texto):
    """
    1. Extrai o trecho que começa com "SDP" até a próxima quebra de linha ou fim.
    2. Remove todos os caracteres não alfanuméricos (só mantém letras e números).
    
    Args:
        texto (str): Texto original para busca e limpeza.
    
    Returns:
        str: Trecho limpo (apenas letras e números) ou None se "SDP" não existir.
    """
    # Passo 1: Extrair o trecho "SDP" até \n ou fim
    match = re.search(r'(SDP.*?)(\n|$)', texto, re.DOTALL)
    if not match:
        return None
    
    trecho_sdp = match.group(1)
    
    # Passo 2: Remover caracteres especiais (só manter letras e números)
    trecho_limpo = re.sub(r'[^a-zA-Z0-9]', '', trecho_sdp)
    
    return f"{trecho_limpo[:3]} {trecho_limpo[3:5]}"





def extrair_titulo(texto):
    """
    Extrai o trecho do texto que começa com "SDP" até o final.
    
    Args:
        texto (str): O texto original a ser processado.
    
    Returns:
        str: O texto a partir de "SDP" até o final, ou None se não encontrar.
    """
    match = re.search(r'(SDP.*)', texto)
    return match.group(1) if match else None



if __name__ == "__main__":

    # Criar a janela de seleção de arquivo
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal

    # Selecionar múltiplos arquivos PDF
    file_paths = filedialog.askopenfilenames(title="Selecione um ou mais arquivos PDF", filetypes=[("Arquivos PDF", "*.pdf")])
    

    # Iterar sobre os arquivos selecionados
    for file_path in file_paths:
        
        arquivo = extrair_titulo(file_path)

        # Extrai texto do pdf
        texto = extrair_texto_pdf(file_path)

        # print(file_path)
        Parque = extrair_Parque(texto)


        # print(texto)
        Temperatura = extrair_temperatura(texto)
        Umidade = extrair_Umidade(texto,arquivo)
        Poste_e_resistencia = extrair_Poste_e_resistencia(texto)

        # extrair_temperatura_new(texto)
        # extrair_Umidade(texto,arquivo)


        print(f"{arquivo} - {Parque} - {Poste_e_resistencia} - {Temperatura} - {Umidade}")  # Imprime o Parque seguido da linha filtrada

        # print(Umidade)
        # extrair_Umidade(texto)

        # extrair_Tempo(texto)

        # print(f"{arquivo} - {Parque}")

        # # Extrai o texto e filtra as linhas com "70mm"
        # texto_70mm = filtrar_linhas_com_70mm(texto) 
        
        # # print(texto_70mm)

        # if texto_70mm:
        #     for linha in texto_70mm:
        #         print(f"{arquivo} - {Parque} - {linha}")  # Imprime o Parque seguido da linha filtrada
        # else:
        #     print(f"{Parque} - Nenhuma linha com '70mm' encontrada.")