import cv2

def tratarImagem(imagem):
    """
    Função para tratar a imagem antes de aplicar ao OCR.
    """    
    # Carrega a imagem
    imagem = cv2.imread(imagem)
    # Verifica se a imagem foi carregada corretamente
    if imagem is None:
        raise ValueError("Imagem não encontrada ou caminho inválido.")
    
    # Redimensiona a imagem
    imagem = cv2.resize(imagem, (800, 600))
    # Converte a imagem para escala de cinza
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    # Remoção de ruído
    imagem = cv2.medianBlur(imagem, 3)
    # Aplica um filtro de desfoque
    imagem = cv2.GaussianBlur(imagem, (5, 5), 0)
    # Binarização adaptativa
    imagem = cv2.adaptiveThreshold(imagem, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)
    
    return imagem
    
def tratarImagem_cv2(imagem):
    """
    Recebe uma imagem já carregada em formato OpenCV (np.array)
    e aplica os mesmos tratamentos da função tratarImagem().
    """
    if imagem is None:
        raise ValueError("Imagem inválida (None) recebida.")
    
    imagem = cv2.resize(imagem, (800, 600))
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagem = cv2.medianBlur(imagem, 3)
    imagem = cv2.GaussianBlur(imagem, (5, 5), 0)
    imagem = cv2.adaptiveThreshold(imagem, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)
    
    return imagem