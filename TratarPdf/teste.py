import PyPDF2

def dividir_pdf_por_tuplas(arquivo_pdf, intervalos):
    # Criar um objeto PDF Reader
    with open(arquivo_pdf, 'rb') as arquivo:
        pdf_reader = PyPDF2.PdfReader(arquivo)
        
        # Criar grupos de páginas baseados nas tuplas
        for i, (inicio, fim) in enumerate(intervalos):
            # Criar um objeto PDF Writer
            pdf_writer = PyPDF2.PdfWriter()
            
            # Adicionar as páginas do intervalo ao writer
            for pagina in range(inicio, fim + 1):
                if pagina < len(pdf_reader.pages):  # Verificar se a página existe
                    pdf_writer.add_page(pdf_reader.pages[pagina])
            
            # Criar um nome para o novo arquivo PDF
            novo_arquivo_pdf = f'grupo_{i + 1}.pdf'
            
            # Salvar o grupo de páginas como um novo arquivo PDF
            with open(novo_arquivo_pdf, 'wb') as novo_arquivo:
                pdf_writer.write(novo_arquivo)

    print("Divisão de PDF em intervalos com tuplas concluída!")

# Exemplo de uso
intervalos = [(0, 2), (3, 8), (9, 14), (15, 20), (21, 23), (24, 26), (27, 31), (32, 38), (39, 43), (44, 46), (47, 53), (54, 58), (59, 65), (66, 71), (72, 75), (76, 78), (79, 82), (83, 86), (87, 90), (91, 94), (95, 98), (99, 102), (103, 106), (107, 110), (111, 113), (114, 116), (117, 119), (120, 122), (123, 125), (126, 132), (133, 135), (136, 138), (139, 141), (142, 144), (145, 147), (148, 155), (156, 160), (161, 169), (170, 178), (179, 186), (187, 190), (191, 194), (195, 197), (198, 200), (201, 203), (204, 206), (207, 209), (210, 213), (214, 219)]  # Define os intervalos de páginas


# dividir_pdf_por_tuplas('TratarPdf\PDF\FormularioRealizado1.pdf', intervalos)

print(len(intervalos))