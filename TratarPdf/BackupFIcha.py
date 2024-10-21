import PyPDF2
import re

class Ficha:
    def __init__(self,filepath,parque=None,poste=None,tipo=None):
        self.parque = parque
        self.poste = poste
        self.tipo = tipo
        self.filepath = self.OpenPDF(filepath)

    def OpenPDF(self,file_path):
        identificador = ""
        with open(file_path, 'rb') as file:
            pdf = PyPDF2.PdfReader(file)
            print(f"Type: {type(pdf)}")
            text_complete = ""

            # Extraindo o texto de cada página
            for numb_pag, page in enumerate(pdf.pages):
                text = page.extract_text()
                text_complete += f"\n--- Página {numb_pag + 1} ---\n{text}"
            
            # print(text_complete)

            for line in text_complete.splitlines():
                if line.startswith("Identificador"):
                    identificador = line.replace("Identificador ","")
                    
                    self._Separe_identificador(identificador)

            for line in text_complete.splitlines():
                if line.startswith("Inspeção"):
                    inspecao = line.replace("Inspeção: ","")
                    
                    self._Separe_inspecao(inspecao)
        return file_path

    def _Separe_identificador(self,identificador):
        self.poste = self.regex_Poste(identificador)
        self.parque = self.regex_Parque(identificador)

    def _Separe_inspecao(self,inspecao):
        self.tipo = self.regex_Tipo(inspecao)

    def regex_Poste(self,identificador):
        padrao = r"P\.[^ -]+"
        Poste = re.search(padrao, identificador)
        return Poste.group(0) if Poste else None

    def regex_Parque(self,identificador):
        # Usar regex para remover tudo a partir de "P. ", incluindo "P." e o restante
        padrao = r"P\..*"
        texto_limpo = re.sub(padrao, "", identificador).strip()
        
        # Remover espaços, hífens e zeros
        texto_limpo = re.sub(r"[ -]", "", texto_limpo)

        # Adicionar um espaço entre a parte alfabética e a numérica
        texto_com_espaco = re.sub(r"([A-Za-z])(\d+)", r"\1 \2", texto_limpo)
        
        # Formatar a parte numérica para ter dois dígitos
        texto_formatado = re.sub(r" (\d+)", lambda match: f" {int(match.group(1)):02}", texto_com_espaco)
        
        return texto_formatado

    def regex_Tipo(self,inspecao):
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
        return None  # Retorna None se nenhuma chave for encontrada
        ...

    def renomear_pdf(self,new_file):
        ...