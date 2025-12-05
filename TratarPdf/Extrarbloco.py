import tkinter as tk
from tkinter import ttk, filedialog
import ezdxf

class DWGBlocosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Extrator de Blocos DWG")
        self.root.geometry("600x400")

        # Variáveis
        self.arquivo_dwg = None
        self.blocos = []

        # Widgets
        self.criar_widgets()

    def criar_widgets(self):
        # Frame principal
        frame = ttk.Frame(self.root, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        # Botão para selecionar arquivo
        ttk.Button(
            frame, 
            text="Selecionar Arquivo DWG", 
            command=self.selecionar_arquivo
        ).pack(pady=10)

        # Árvore para listar blocos
        self.tree = ttk.Treeview(frame, columns=("Nome", "Layer", "Coordenadas"), show="headings")
        self.tree.heading("Nome", text="Nome do Bloco")
        self.tree.heading("Layer", text="Layer")
        self.tree.heading("Coordenadas", text="Coordenadas (X, Y)")
        self.tree.pack(fill=tk.BOTH, expand=True)

    def selecionar_arquivo(self):
        # Abre diálogo para selecionar arquivo
        self.arquivo_dwg = filedialog.askopenfilename(
            title="Selecione um DWG",
            filetypes=[("Arquivos DWG", "*.dwg"), ("Todos os arquivos", "*.*")]
        )

        if self.arquivo_dwg:
            self.listar_blocos()

    def listar_blocos(self):
        # Limpa a árvore
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            # Abre o arquivo DWG com ezdxf
            doc = ezdxf.readfile(self.arquivo_dwg)
            msp = doc.modelspace()

            # Filtra blocos do tipo INSERT
            blocos = [ent for ent in msp if ent.dxftype() == 'INSERT']

            # Adiciona à lista
            for bloco in blocos:
                nome = bloco.dxf.name
                layer = bloco.dxf.layer
                x, y, _ = bloco.dxf.insert  # Coordenadas (ignora Z)
                self.tree.insert("", tk.END, values=(nome, layer, f"({x:.2f}, {y:.2f})"))

        except Exception as e:
            tk.messagebox.showerror("Erro", f"Não foi possível ler o arquivo:\n{str(e)}")

# Inicia a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = DWGBlocosApp(root)
    root.mainloop()