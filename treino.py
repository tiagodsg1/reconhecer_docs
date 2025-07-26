from functions.carregarDataset import carregar_dataset
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Carregar os dados
X_texto, y_rotulo = carregar_dataset("dataset")
print(f"Total de documentos processados: {len(X_texto)}")

modelo = make_pipeline(
    TfidfVectorizer(),
    LogisticRegression(max_iter=1000)
)

modelo.fit(X_texto, y_rotulo)

joblib.dump(modelo, "modelo_documento.pkl")
print("✅ Modelo salvo como 'modelo_documento.pkl'")