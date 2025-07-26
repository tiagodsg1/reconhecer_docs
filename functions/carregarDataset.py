import os
from functions.lerImagem import extrair_texto
from functions.tratarImagem import tratarImagem

def carregar_dataset(diretorio_base):
    X_texto = []
    y_rotulo = []

    for rotulo in os.listdir(diretorio_base):
        pasta = os.path.join(diretorio_base, rotulo)
        if not os.path.isdir(pasta):
            continue
        
        for nome_arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, nome_arquivo)
            if not caminho_arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
                continue

            try:
                imagem = tratarImagem(caminho_arquivo)
                texto = extrair_texto(imagem)
                X_texto.append(texto)
                y_rotulo.append(rotulo)
            except Exception as e:
                print(f"Erro ao processar {caminho_arquivo}: {e}")

    return X_texto, y_rotulo