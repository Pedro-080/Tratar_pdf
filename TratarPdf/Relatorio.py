from Ficha import Ficha
import PyPDF2

class Relatorio:
    def __init__(self, caminho_pdf):
        self.caminho_pdf = self.OpenPDF(caminho_pdf)
        self.fichas = []

    def OpenPDF(self,file_path):
        identificador = ""
        paginas = dict()
        # print(f"type: {self.fichas}")

        with open(file_path, 'rb') as file:
            pdf = PyPDF2.PdfReader(file)
            text_complete = ""

            # Extraindo o texto de cada página
            for numb_pag, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text.count("Identificador") != 0:
                    paginas[numb_pag]=text

            paginas[len(pdf.pages)-1]=""
            
            intervalo = self._criar_intervalos(paginas)

            # print(intervalo)

            # print(f" {len(self._criar_intervalos(paginas))}")
           

            # print(f"{len(paginas)} keys: {paginas.keys()}")

            # num_fichas_no_pdf = text_complete.count("Identificador")
            
            # print(f"{paginas[0]}")

            for pagina, text in list(paginas.items())[:-1]:
                for line in text.splitlines():
                    if line.startswith("Identificador"):
                        identificador = line.replace("Identificador ","")

                    if line.startswith("Inspeção"):
                        inspecao = line.replace("Inspeção: ","")
                        
                
                ficha = Ficha(identificador,inspecao,intervalo[pagina])

                # self.fichas.append(ficha)
                

                # print(f"{ficha.parque} - {ficha.poste} - {ficha.tipo} - {ficha.paginas} - {ficha.setor}")




                

            # if len(paginas) == 1:
            #     # num_fichas_no_pdf = self._contar_fichas(text_complete) -> Mais lento que o .count

            #     # print(f"Identificador: {num_fichas_no_pdf}")

            #     for line in text_complete.splitlines():
            #         if line.startswith("Identificador"):
            #             identificador = line.replace("Identificador ","")
                        
            #             self._Separe_identificador(identificador)

            #     for line in text_complete.splitlines():
            #         if line.startswith("Inspeção"):
            #             inspecao = line.replace("Inspeção: ","")
                        
            #             self._Separe_inspecao(inspecao)
            # else:
            #     print(f"O arquivo {file_path} possui mais de uma ficha.")

        return file_path
    
        
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