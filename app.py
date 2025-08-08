import joblib, os
from functions.lerImagem import extrair_texto
from functions.tratarImagem import tratarImagem, tratarImagem_cv2

class DocumentoClassifier:
    def __init__(self, imagem):
        # Carrega o modelo previamente treinado
        self.modelo = joblib.load("modelo_documento.pkl")
        self.imagem = imagem
        tipo = self.classificar()
        print(tipo)



    def classificar(self):
        # Usar para prever
        nova_img = tratarImagem_cv2(self.imagem)
        novo_texto = extrair_texto(nova_img)
        predicao = self.modelo.predict([novo_texto])[0]
        return predicao
    
DocumentoClassifier("C:/Users/tiago/Documentos/GitHub/reconhecer_docs/dataset/Carteira_Trabalho/CTPS 01.jpeg")