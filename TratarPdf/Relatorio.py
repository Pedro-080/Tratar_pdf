from Ficha import Ficha
import PyPDF2
import os

class Relatorio:
    def __init__(self, caminho_pdf):
        self.caminho_pdf = caminho_pdf
        self.lista_de_fichas = self.OpenPDF(caminho_pdf)

    def OpenPDF(self,file_path):
        identificador = ""
        paginas = dict()  

        with open(file_path, 'rb') as file:
            lista_de_fichas = []
            leitor_pdf = PyPDF2.PdfReader(file)
            text_complete = ""
            
            # Extraindo o texto de cada página
            for numb_pag, page in enumerate(leitor_pdf.pages):
                text = page.extract_text()
                if text.count("Identificador") != 0:
                    paginas[numb_pag]=text

            paginas[len(leitor_pdf.pages)-1]=""
            
            intervalo = self._criar_intervalos(paginas)

            for pagina, text in list(paginas.items())[:-1]:
                for line in text.splitlines():
                    if line.startswith("Identificador"):
                        identificador = line.replace("Identificador ","")

                    if line.startswith("Inspeção"):
                        inspecao = line.replace("Inspeção: ","")
                        
                ficha = Ficha(identificador,inspecao,intervalo[pagina])

                lista_de_fichas.append(ficha)
            
        return lista_de_fichas
    
    # # Função de teste
    # def Get_fichas(self):
    #     print(f"Fichas: {self.fichas}")

    def _criar_intervalos(self,dicionario):
        # Obter as chaves e ordenar
        chaves = sorted(dicionario.keys())
        
        # Criar a lista de tuplas
        intervalos = {}
        for i in range(len(chaves) - 1):
            if i < len(chaves)-2:
                intervalo = (chaves[i], chaves[i + 1] - 1)
            else:
                intervalo = (chaves[i], chaves[i + 1])

            intervalos[chaves[i]] = intervalo

            # intervalos.append(intervalo)
        
        return intervalos

    def test(self):
    # for ficha in self.lista_de_fichas:
        print(f"aquiiiii:{self.caminho_pdf}")


    def Salvar_Relatorio(self,save_path):
        #Define uma variavel local como copia do atributo de classe
        lista_de_fichas = self.lista_de_fichas
        
        lista_de_fichas_filtrada = [ficha for ficha in lista_de_fichas if ficha.setor == "Qualidade"]

        #Extrai as fichas 
        lista_de_fichas = self.Extrair_fichas(lista_de_fichas_filtrada)

        for ficha in lista_de_fichas_filtrada:
            print(ficha)
            self.Salvar_arquivo(ficha,save_path)
        
        ...
        

    def Extrair_fichas(self,lista_de_fichas):

        with open(self.caminho_pdf, 'rb') as file:
            leitor_pdf = PyPDF2.PdfReader(file)

            for fixa in lista_de_fichas:
                # Cria um objeto PDF Writer para escrever o novo arquivo
                escritor_pdf = PyPDF2.PdfWriter()

                # Filtra as fichas de Qualidade
                if fixa.setor == "Qualidade":

                    # Adiciona as páginas do PDF original ao novo arquivo, de acordo com os intervalos
                    for i in range(fixa.paginas[0], fixa.paginas[1] + 1):

                        escritor_pdf.add_page(leitor_pdf.pages[i])
                        fixa.Add_pagina(escritor_pdf)

                    # self.Salvar_fichas(fixa,file_path)

        return lista_de_fichas



    def Salvar_arquivo(self,ficha,save_path):

        # caminho_raiz = os.path.dirname(file_path)
        
        nova_pasta = ficha.parque + " - " + ficha.poste.replace("/",".")
        
        caminho_nova = f"{save_path}/Fichas/{ficha.parque}/{nova_pasta}"

        self._criar_pasta(caminho_nova)

        novo_arquivo = caminho_nova +"/"+nova_pasta+" - " + ficha.tipo +".pdf"

        # print(f"{ficha.parque} - {ficha.poste} - {ficha.tipo} - {ficha.paginas} - {ficha.setor} | {novo_arquivo}")
        # print(f"novo nome: {novo_nome}")
        # novo_nome = 

        with open(novo_arquivo, 'wb') as new_file:
            ficha.PDF.write(new_file)

    
    def _criar_pasta(self,caminho_nova):
        try:
            # Cria a pasta, se ela não existir
            os.makedirs(caminho_nova, exist_ok=True)
            # print(f'A pasta "{caminho_nova}" foi criada ou já existia.')
            ...
        except Exception as e:
            # print(f'Erro ao criar a pasta: {e}')
            ...


#   def salvar_arquivo(self,ficha,file_path):

#         caminho_raiz = os.path.dirname(file_path)
        
#         nova_pasta = ficha.parque + " - " + ficha.poste.replace("/",".")
        
#         caminho_nova = f"{caminho_raiz}/Fichas/{ficha.parque}/{nova_pasta}"

#         self._criar_pasta(caminho_nova)

#         novo_arquivo = caminho_nova +"/"+nova_pasta+" - " + ficha.tipo +".pdf"

#         print(f"{ficha.parque} - {ficha.poste} - {ficha.tipo} - {ficha.paginas} - {ficha.setor} | {novo_arquivo}")
#         # print(f"novo nome: {novo_nome}")
#         # novo_nome = 

#         with open(novo_arquivo, 'wb') as new_file:
#             ficha.PDF.write(new_file)