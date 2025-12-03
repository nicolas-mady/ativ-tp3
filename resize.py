
from PIL import Image
import os

# Pasta das imagens
folder = "images"
# Imagem de referência
ref_img = os.path.join(folder, "Cópia de IMG_2347.JPG")

# Verifica se a imagem de referência existe
if not os.path.exists(ref_img):
    print(f"Imagem de referência '{ref_img}' não encontrada.")
    exit(1)

# Obtém tamanho da referência
with Image.open(ref_img) as ref:
    ref_size = ref.size

# Redimensiona todas as imagens JPG
for fname in os.listdir(folder):
    if not fname.startswith("Cópia"):
        path = os.path.join(folder, fname)
        try:
            with Image.open(path) as img:
                img_resized = img.resize(ref_size, Image.LANCZOS)
                # Salva sobrescrevendo
                img_resized.save(path)
                print(f"Redimensionada: {fname}")
        except Exception as e:
            print(f"Erro em {fname}: {e}")
