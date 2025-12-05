import PyPDF2
from tkinter import Tk, filedialog

def selecionar_pdf():
    """Abre a janela de seleção de arquivos e retorna um PDF escolhido"""
    root = Tk()
    root.withdraw()
    
    arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo PDF",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )
    
    return arquivo

def extrair_texto_pdf(caminho_pdf):
    """Extrai texto de um arquivo PDF"""
    with open(caminho_pdf, 'rb') as arquivo:
        leitor = PyPDF2.PdfReader(arquivo)
        texto_completo = ""
        
        for pagina in range(len(leitor.pages)):
            texto_pagina = leitor.pages[pagina].extract_text()
            texto_completo += f"\n--- Página {pagina + 1} ---\n"
            texto_completo += texto_pagina
        
        return texto_completo

# Selecionar o PDF
arquivo_pdf = selecionar_pdf()

if arquivo_pdf:
    # Extrair e mostrar o texto
    texto = extrair_texto_pdf(arquivo_pdf)
    print(texto)
else:
    print("Nenhum arquivo selecionado.")