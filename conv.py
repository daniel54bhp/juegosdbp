import os
import unicodedata
import re
from PIL import Image # Necesitas instalar Pillow: pip install Pillow

def normalize_text_for_filename(text):
    """
    Normaliza un texto para usarlo como nombre de archivo base:
    - Convierte a minúsculas.
    - Elimina acentos.
    - Elimina espacios.
    - Elimina caracteres no alfanuméricos.
    """
    s = text.lower()
    s = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
    s = re.sub(r'\s+', '', s) # Elimina espacios (uno o más)
    s = re.sub(r'[^a-z0-9]', '', s) # Elimina cualquier cosa que no sea letra o número
    return s

def convert_images_in_folder(folder_path, delete_originals=False):
    """
    Convierte imágenes .jpg y .jpeg en una carpeta a .png con nombres normalizados.
    """
    if not os.path.isdir(folder_path):
        print(f"Error: La carpeta '{folder_path}' no existe.")
        return

    print(f"Procesando imágenes en la carpeta: '{folder_path}'")
    converted_count = 0
    error_count = 0

    for filename_original in os.listdir(folder_path):
        original_file_path = os.path.join(folder_path, filename_original)

        if os.path.isfile(original_file_path):
            base_name_original, ext_original = os.path.splitext(filename_original)
            ext_original_lower = ext_original.lower()

            if ext_original_lower in ['.jpg', '.jpeg']:
                try:
                    # Normalizar el nombre base del archivo
                    normalized_base_name = normalize_text_for_filename(base_name_original)
                    
                    # Nuevo nombre de archivo con extensión .png
                    new_filename_png = normalized_base_name + ".png"
                    new_file_path_png = os.path.join(folder_path, new_filename_png)

                    # Abrir la imagen original
                    img = Image.open(original_file_path)
                    
                    # Convertir y guardar como PNG
                    # Asegurarse de que si la imagen tiene canal Alfa (como algunos JPEGs o PNGs guardados como JPG),
                    # se maneje correctamente al guardar como PNG.
                    if img.mode == 'RGBA' or 'A' in img.getbands():
                        img.save(new_file_path_png, 'PNG')
                    else:
                        img.convert('RGB').save(new_file_path_png, 'PNG')
                    
                    print(f"Convertido: '{filename_original}' -> '{new_filename_png}'")
                    converted_count += 1

                    # Opcionalmente, eliminar el archivo original
                    if delete_originals:
                        # Primero cerrar la imagen para liberar el archivo
                        img.close() 
                        os.remove(original_file_path)
                        print(f"Eliminado original: '{filename_original}'")
                    else:
                        img.close()

                except Exception as e:
                    print(f"Error al procesar '{filename_original}': {e}")
                    error_count += 1
            # else:
                # print(f"Omitido (no es JPG/JPEG): '{filename_original}'")

    print(f"\nProceso completado.")
    print(f"Imágenes convertidas: {converted_count}")
    print(f"Errores: {error_count}")

if __name__ == "__main__":
    # --- INSTRUCCIONES DE USO ---
    # 1. Asegúrate de tener Python instalado.
    # 2. Instala la librería Pillow: Abre una terminal o CMD y escribe: pip install Pillow
    # 3. Guarda este script como un archivo .py (ej. convertir_imagenes.py).
    # 4. CAMBIA LA RUTA de 'target_folder' a la carpeta donde están tus imágenes (ej. "src" o "ruta/a/tus/imagenes").
    # 5. Ejecuta el script desde la terminal: python convertir_imagenes.py
    # 6. Revisa la opción 'delete_original_files'. Por defecto es False (no borra).
    #    Cámbiala a True si quieres borrar los JPG/JPEG originales después de convertirlos.
    #    ¡HAZ UNA COPIA DE SEGURIDAD ANTES SI VAS A BORRAR ORIGINALES!

    target_folder = "src" # <<< CAMBIA ESTO a la ruta de tu carpeta de imágenes
    
    # --- Advertencia sobre eliminación ---
    print("ADVERTENCIA: Este script puede modificar y eliminar archivos.")
    print("Se recomienda hacer una COPIA DE SEGURIDAD de tu carpeta de imágenes antes de continuar,")
    print("especialmente si planeas activar la eliminación de archivos originales.\n")

    # Preguntar al usuario si desea eliminar los originales
    choice = input("¿Deseas eliminar los archivos .jpg/.jpeg originales después de la conversión? (s/N): ").lower()
    delete_original_files = choice == 's'

    if delete_original_files:
        print("\n¡ATENCIÓN! Los archivos originales .jpg/.jpeg SERÁN ELIMINADOS después de la conversión.")
        confirm = input("Confirma esta acción escribiendo 'SI': ")
        if confirm != "SI":
            print("Eliminación no confirmada. Los archivos originales no se borrarán.")
            delete_original_files = False
        else:
            print("Eliminación confirmada.")
    else:
        print("\nLos archivos originales .jpg/.jpeg NO se eliminarán.")

    convert_images_in_folder(target_folder, delete_original_files)