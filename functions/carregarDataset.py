import os, fitz, cv2
from pdf2image import convert_from_path
import numpy as np

from functions.lerImagem import extrair_texto
from functions.tratarImagem import tratarImagem , tratarImagem_cv2

import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def carregar_dataset(diretorio_base):
    x_texto = []
    y_rotulo = []

    for rotulo in os.listdir(diretorio_base):
        pasta = os.path.join(diretorio_base, rotulo)
        if not os.path.isdir(pasta):
            continue
        
        for nome_arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, nome_arquivo)
            try:
                if caminho_arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
                    imagem = tratarImagem(caminho_arquivo)
                    texto = extrair_texto(imagem)
                    x_texto.append(texto)
                    y_rotulo.append(rotulo)
                elif caminho_arquivo.lower().endswith('.pdf'):
                    texto_pdf = extrair_texto_pdf(caminho_arquivo)
                    if texto_pdf:
                        x_texto.append(texto_pdf)
                        y_rotulo.append(rotulo)
                    else:
                        imagens_pdf = convert_from_path(caminho_arquivo, poppler_path=r"C:\poppler-24.08.0\Library\bin")
                        texto_total = ""
                        for imagem_pil in imagens_pdf:
                            imagem_cv = cv2.cvtColor(np.array(imagem_pil), cv2.COLOR_RGB2BGR)
                            imagem_tratada = tratarImagem_cv2(imagem_cv)
                            texto_total += extrair_texto(imagem_tratada) + "\n"

                        x_texto.append(texto_total)
                        y_rotulo.append(rotulo)

            except Exception as e:
                print(f"Erro ao processar {caminho_arquivo}: {e}")

    return x_texto, y_rotulo

def extrair_texto_pdf(caminho_pdf):
    doc = fitz.open(caminho_pdf)
    texto_total = ""
    for pagina in doc:
        texto = pagina.get_text().strip()
        if texto:
            texto_total += texto + "\n"
    doc.close()
    return texto_total if texto_total.strip() else None