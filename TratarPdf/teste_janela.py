import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os

def selecionar_arquivos():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    arquivos_origem = filedialog.askopenfilenames(title="Selecione os arquivos para copiar")
    return arquivos_origem

def selecionar_destino():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    destino = filedialog.askdirectory(title="Selecione o diretório de destino")
    return destino

def copiar_arquivos():
    arquivos_origem = selecionar_arquivos()
    print(f"arquivos: {arquivos_origem}")

    if not arquivos_origem:
        return
    
    destino = selecionar_destino()
    if not destino:
        return

    for arquivo_origem in arquivos_origem:
        nome_arquivo = os.path.basename(arquivo_origem)
        destino_final = os.path.join(destino, nome_arquivo)
        shutil.copy(arquivo_origem, destino_final)

    messagebox.showinfo("Sucesso", f"{len(arquivos_origem)} arquivos copiados para {destino}")

if __name__ == "__main__":
    copiar_arquivos()
