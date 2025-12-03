import os
from PIL import Image

def convert_to_jpg(image_folder):
    for filename in os.listdir(image_folder):
        file_path = os.path.join(image_folder, filename)
        name, ext = os.path.splitext(filename)
        ext_lower = ext.lower()
        # Ignora arquivos que já são .jpg
        if ext_lower == ".jpg":
            continue
        # Converte apenas arquivos de imagem conhecidos
        if ext_lower in [".jpeg", ".jpg", ".png", ".heic", ".dng", ".bmp", ".tiff", ".tif", ".JPG", ".HEIC", ".DNG"]:
            try:
                with Image.open(file_path) as img:
                    rgb_img = img.convert("RGB")
                    new_path = os.path.join(image_folder, f"{name}.jpg")
                    rgb_img.save(new_path, "JPEG")
                    print(f"Convertido: {filename} -> {name}.jpg")
            except Exception as e:
                print(f"Erro ao converter {filename}: {e}")

if __name__ == "__main__":
    convert_to_jpg("images")
