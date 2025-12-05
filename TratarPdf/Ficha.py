import re

class Ficha:
    def __init__(self,identificador,inspecao,paginas,PDF=None):
        self.identificador = identificador
        self.inspecao = inspecao
        self.parque = self.regex_Parque(identificador)
        self.poste = self.regex_Poste(identificador)
        self.tipo = self.regex_Tipo(inspecao)
        self.setor = self.regex_Setor(inspecao)
        self.paginas = paginas
        self.PDF = PDF

    def __str__(self):
        return f"{self.parque} - {self.poste} - {self.tipo} - {self.setor} - pág:{self.paginas}"
        # return f"pág:{self.paginas} {self.identificador}"

    def regex_Poste(self,identificador):
        # padrao = r"P\.[^ -]+"
        # Poste = re.search(padrao, identificador)
        Poste = self.Extrair_poste(identificador)

        if Poste != None:
            Poste = Poste.replace(" ","")

        # return Poste.group(0) if Poste else None
        return Poste

    def regex_Parque(self,identificador):
        # Usar regex para remover tudo antes de "SDP" e tudo a partir de "P."
        padrao = r".*?(SDP.*?)(P\..*)?$"
        texto_limpo = re.sub(padrao, r"\1", identificador,flags=re.IGNORECASE).strip()
        
        # Remover espaços, hífens e zeros
        texto_limpo = re.sub(r"[ -]", "", texto_limpo)

        # Adicionar um espaço entre a parte alfabética e a numérica
        texto_com_espaco = re.sub(r"([A-Za-z])(\d+)", r"\1 \2", texto_limpo)
        
        # Formatar a parte numérica para ter dois dígitos
        texto_formatado = re.sub(r" (\d+)", lambda match: f" {int(match.group(1)):02}", texto_com_espaco)
        
        texto_formatado = texto_formatado[:6].upper()

        return texto_formatado

    def regex_Tipo(self,inspecao):
        tipos_fichas = {
            "IMP": "Implantação",
            "FUN": "Fundação",
            "REP": "Reparo",
            "ESC": "Escavação",
            "LAN": "Lançamento",
            "INS": "Inspeção",
            "TOPOGRAFIA":"Topografia"
        }

        # Cria um padrão de regex para buscar qualquer chave do dicionário
        pattern = re.compile("|".join(re.escape(key) for key in tipos_fichas.keys()))

        # Procura por uma correspondência na string e substitui pelo valor correspondente
        match = pattern.search(inspecao)

        if match:
            return tipos_fichas[match.group()]
        return None  # Retorna None se nenhuma chave for encontrada
        ...

    def regex_Setor(self,inspecao):
        setores = {
            "QUA": "Qualidade",
            "SMS": "Meio ambiente",
        }

        # Cria um padrão de regex para buscar qualquer chave do dicionário
        pattern = re.compile("|".join(re.escape(key) for key in setores.keys()))

        # Procura por uma correspondência na string e substitui pelo valor correspondente
        match = pattern.search(inspecao)

        if match:
            return setores[match.group()]
        return None  # Retorna None se nenhuma chave for encontrada
        
    def Add_pagina(self,PDF):
        self.PDF = PDF


    def Extrair_poste(self,text):
        text = text.upper()

        # Encontrar a segunda ocorrência de "P"
        pos_p2 = text.find("P", text.find("P") + 1)
        if pos_p2 == -1:
            # return "Segundo 'P' não encontrado."
            return None

        # Encontrar a primeira ocorrência de "/"
        pos_barra = text.find("/")
        if pos_barra == -1:
            # return "Primeira '/' não encontrada."
            return None

        # Calcular a posição final (2 posições além da primeira '/')
        pos_final = pos_barra + 3

        # Extrair o texto entre o segundo 'P' e a posição final
        texto_extraido = text[pos_p2:pos_final]
        return texto_extraido