import cv2

# Cargar imagen
imagen = cv2.imread(r'C:\temp\WIN_20240718_15_18_27_Pro.jpg')
# Verificar que la imagen se haya cargado
if imagen is None:
    print("Error: No se pudo cargar la imagen. Revisa la ruta del archivo.")
else:
    # Obtener dimensiones de la pantalla
    screen_res = (800, 600)  # Puedes cambiarlo a la resolución de tu pantalla

    # Redimensionar manteniendo la proporción
    alto, ancho = imagen.shape[:2]
    factor = min(screen_res[0] / ancho, screen_res[1] / alto)
    nuevo_ancho = int(ancho * factor)
    nuevo_alto = int(alto * factor)

    imagen_redimensionada = cv2.resize(imagen, (nuevo_ancho, nuevo_alto))

    # Mostrar imagen
    cv2.imshow('Imagen Ajustada', imagen_redimensionada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()