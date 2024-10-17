import pytesseract
from PIL import Image

# Configurar o caminho para o executável do Tesseract (ajuste conforme o seu sistema)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows
# Em sistemas Unix (Linux/Mac), normalmente o tesseract está no PATH, então isso pode ser omitido

# Carregar a imagem de teste
imagem = Image.new('RGB', (200, 100), color = (255, 255, 255))
# Adicionar texto à imagem
from PIL import ImageDraw, ImageFont
draw = ImageDraw.Draw(imagem)
draw.text((10, 40), "Hello, World!", fill=(0, 0, 0))

imagem.show()
# Salvar a imagem temporariamente
imagem.save("hello_world_test.png")

# Ler a imagem com o pytesseract
texto_extraido = pytesseract.image_to_string(imagem)

# Exibir o resultado
print("Texto extraído:", texto_extraido)