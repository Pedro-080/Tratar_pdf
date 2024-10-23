import PyPDF2
import re
import os

class Ficha:
    def __init__(self,filepath,parque=None,poste=None,tipo=None):
        self.parque = parque
        self.poste = poste
        self.tipo = tipo
        self.filepath = self.OpenPDF(filepath)

    def OpenPDF(self,file_path):
        identificador = ""
        paginas = dict()

        with open(file_path, 'rb') as file:
            pdf = PyPDF2.PdfReader(file)
            text_complete = ""

            # Extraindo o texto de cada página
            for numb_pag, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text.count("Identificador") != 0:
                    paginas[numb_pag]=text

                text_complete += f"\n--- Página {numb_pag + 1} ---\n{text}" # -> Deletar
            
            # print(f"{len(paginas)} keys: {paginas.keys()}")

            # num_fichas_no_pdf = text_complete.count("Identificador")
            
            # print(f"{paginas[0]}")

            for pagina, text in paginas.items():
                for line in text.splitlines():
                    if line.startswith("Identificador"):
                        identificador = line.replace("Identificador ","")
                    
                        self._Separe_identificador(identificador)

                    if line.startswith("Inspeção"):
                        inspecao = line.replace("Inspeção: ","")
                        
                        self._Separe_inspecao(inspecao)                    
                    
                    

                    # print(f"{identificador} | {self.parque} - {self.poste} - {self.tipo}")

            print(f" {len(self._criar_intervalos(paginas))}")
                

            if len(paginas) == 1:
                # num_fichas_no_pdf = self._contar_fichas(text_complete) -> Mais lento que o .count

                # print(f"Identificador: {num_fichas_no_pdf}")

                for line in text_complete.splitlines():
                    if line.startswith("Identificador"):
                        identificador = line.replace("Identificador ","")
                        
                        self._Separe_identificador(identificador)

                for line in text_complete.splitlines():
                    if line.startswith("Inspeção"):
                        inspecao = line.replace("Inspeção: ","")
                        
                        self._Separe_inspecao(inspecao)
            else:
                print(f"O arquivo {file_path} possui mais de uma ficha.")

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
        # Usar regex para remover tudo antes de "SDP" e tudo a partir de "P."
        padrao = r".*?(SDP.*?)(P\..*)?$"
        texto_limpo = re.sub(padrao, r"\1", identificador).strip()
        
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

    def renomear_pdf(self):
        caminho_origem = self.filepath
        caminho_raiz = os.path.dirname(self.filepath) 

        folder_path = self.parque + " - " + self.poste.replace("/",".")
        
        caminho_nova = f"{caminho_raiz}/Fichas/{self.parque}/{folder_path}"


        #Cria a pasta do poste
        self._criar_pasta(caminho_nova)


        novo_nome = caminho_nova +"/"+folder_path+" - " + self.tipo +".pdf"
        # print(f"novo_nome: {novo_nome}")

    



        # Verifica se o arquivo já existe
        if os.path.exists(novo_nome):
            print(f'O arquivo {novo_nome} já existe. Nenhuma ação foi realizada.')
            return



        try:
            # Abre o arquivo PDF original para leitura
            with open(caminho_origem, 'rb') as arquivo_origem:
                # Cria um objeto PDF Reader para ler o conteúdo do arquivo
                leitor_pdf = PyPDF2.PdfReader(arquivo_origem)
                
                # Cria um objeto PDF Writer para escrever o novo arquivo
                escritor_pdf = PyPDF2.PdfWriter()

                # Adiciona cada página do PDF original ao novo arquivo
                for pagina in leitor_pdf.pages:
                    escritor_pdf.add_page(pagina)
                
                # Grava o novo arquivo com o nome especificado
                with open(novo_nome, 'wb') as novo_arquivo:
                    escritor_pdf.write(novo_arquivo)
            
            print(f'Arquivo copiado e renomeado para {novo_nome} com sucesso.')
        except Exception as e:
            print(f'Erro ao copiar e renomear o arquivo: {e}')

    def _criar_pasta(self,caminho_nova):
        try:
            # Cria a pasta, se ela não existir
            os.makedirs(caminho_nova, exist_ok=True)
            # print(f'A pasta "{caminho_nova}" foi criada ou já existia.')
            ...
        except Exception as e:
            # print(f'Erro ao criar a pasta: {e}')
            ...

    def _criar_intervalos(self,dicionario):
        # Obter as chaves e ordenar
        chaves = sorted(dicionario.keys())
        
        # Criar a lista de tuplas
        intervalos = []
        for i in range(len(chaves)):
            # O primeiro valor da tupla é a chave atual
            # O segundo valor da tupla é a próxima chave - 1
            intervalo = (chaves[i], chaves[i + 1] - 1)
            intervalos.append(intervalo)
        
        return tuple(intervalos)