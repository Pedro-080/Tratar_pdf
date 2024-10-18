import re

def extrair_p_texto(texto):
    padrao = r"P\.[^ -]+"
    return re.findall(padrao, texto)

def remover_a_partir_de_p(texto):
    # Usar regex para remover tudo a partir de "P. ", incluindo "P." e o restante
    padrao = r"P\..*"
    Poste = re.sub(padrao, "", texto).strip()
    Parque = re.sub(r"[ -]", "", Poste)
    Parque = separar_letras_numeros(Parque)
    return Parque

def separar_letras_numeros(texto):
    # Adicionar um espaço entre a parte alfabética e a numérica
    texto_com_espaco = re.sub(r"([A-Za-z])(\d+)", r"\1 \2", texto)
    # Formatar a parte numérica para ter dois dígitos
    texto_formatado = re.sub(r" (\d+)", lambda match: f" {int(match.group(1)):02}", texto_com_espaco)
    return texto_formatado


# Amostra de entrada
amostra = """
SDP 05 P.3/10 - 12/1000
SDP 07-P.A17/11-15/600-R12-Gel-0218-jose carlos
SDP 07 - P.A18/03  18/2000 - R11 -GEL0229- HUGO  REIS
SDP 07 - P.A18/06  14/2000 - R08 -GEL0229- HUGO  REIS
SDP 10 P.2/05
SDP 5 P.0/10 - 14/600
SDP 5 P.0/11 - 14/600
SDP 5 P.0/12 14/600
SDP07 P.A11/02 17/600
SDP07 P.A16/05 19/1000
SDP07 P.A16/06 18/600
SDP07 P.A16/07 18/600
SDP07-P.A17/10-15/600-R30-Gel-0218-jose carlos
SDP07-P.A18/02-16/600-R16-Gel-0218-jose carlos"""

# Extração dos textos "P.XXXXX"
resultados = extrair_p_texto(amostra)
print(resultados)


# Aplicar a função em cada linha da amostra
linhas_processadas = [remover_a_partir_de_p(linha) for linha in amostra.splitlines()]
for linha in linhas_processadas:
    print(linha)