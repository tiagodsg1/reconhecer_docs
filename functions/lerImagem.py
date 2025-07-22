import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 


def extrair_texto(imagem_cv2):
    texto = pytesseract.image_to_string(imagem_cv2, lang='por')
    return texto