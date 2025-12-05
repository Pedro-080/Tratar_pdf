import os
from PyPDF2 import PdfReader, PdfWriter
from tkinter import Tk, filedialog

def selecionar_pdfs():
    """Abre a janela de seleção de arquivos e retorna os PDFs escolhidos"""
    root = Tk()
    root.withdraw()  # Esconde a janela principal
    
    arquivos = filedialog.askopenfilenames(
        title="Selecione os arquivos PDF",
        filetypes=[("Arquivos PDF", "*.pdf"), ("Todos os arquivos", "*.*")]
    )
    
    return arquivos

def criar_sumario_e_compilar(pdfs):
    """Cria um sumário e compila todos os PDFs em um único arquivo"""
    sumario = []
    pagina_atual = 8  # Começa na página 8 conforme seu ajuste
    escritor = PdfWriter()
    
    for caminho in pdfs:
        nome_arquivo = os.path.basename(caminho)
        pasta = os.path.dirname(caminho)
        
        try:
            with open(caminho, 'rb') as arquivo:
                leitor = PdfReader(arquivo)
                total_paginas = len(leitor.pages)
                
                # Adiciona ao sumário
                sumario.append({
                    'arquivo': nome_arquivo,
                    'inicio': pagina_atual,
                    'fim': pagina_atual + total_paginas - 1,
                    'total': total_paginas
                })
                
                # Adiciona todas as páginas ao PDF compilado
                for pagina in range(total_paginas):
                    escritor.add_page(leitor.pages[pagina])
                
                pagina_atual += total_paginas
                
        except Exception as e:
            print(f"Erro ao processar {nome_arquivo}: {str(e)}")
    
    # Salva o PDF compilado na mesma pasta dos originais
    if pdfs:  # Se há arquivos processados
        caminho_compilado = os.path.join(os.path.dirname(pdfs[0]), "compilado.pdf")
        with open(caminho_compilado, "wb") as arquivo_saida:
            escritor.write(arquivo_saida)
        print(f"\nPDF compilado salvo como: {caminho_compilado}")
    
    return sumario

def imprimir_sumario(sumario):
    """Imprime o sumário formatado no terminal"""
    print("\n" + "="*50)
    print("SUMÁRIO DE DOCUMENTOS".center(50))
    print("="*50)
    print(f"{'Arquivo':<30} {'Início-Fim'}")
    print("-"*50)
    
    for item in sumario:
        print(f"{item['arquivo']:<30} {item['inicio']}-{item['fim']}")
    
    print("="*50 + "\n")

def main():
    print("Selecione os arquivos PDF para criar o sumário e compilar...")
    pdfs = selecionar_pdfs()
    
    if not pdfs:
        print("Nenhum arquivo selecionado. Programa encerrado.")
        return
    
    sumario = criar_sumario_e_compilar(pdfs)
    imprimir_sumario(sumario)

if __name__ == "__main__":
    main()