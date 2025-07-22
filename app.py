import joblib, os
from functions.lerImagem import extrair_texto
from functions.tratarImagem import tratarImagem

class DocumentoClassifier:
    def __init__(self):
        # Carrega o modelo previamente treinado
        self.modelo = joblib.load("modelo_documento.pkl")

    def classificar(self, imagem_path):
        # Usar para prever
        nova_img = tratarImagem(imagem_path)
        novo_texto = extrair_texto(nova_img)
        predicao = self.modelo.predict([novo_texto])[0]
        return predicao