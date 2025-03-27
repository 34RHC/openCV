import cv2
import numpy as np

# Función vacía para los trackbars
def empty(a):
    pass

# Capturar la webcam
cap = cv2.VideoCapture(0)

# Crear una ventana única con trackbars
cv2.namedWindow("Ajustes de Color")
cv2.resizeWindow("Ajustes de Color", 600, 300)

# Crear trackbars con valores iniciales para detectar rojo (puedes cambiarlos)
cv2.createTrackbar("Hue Min", "Ajustes de Color", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Ajustes de Color", 10, 179, empty)
cv2.createTrackbar("Sat Min", "Ajustes de Color", 100, 255, empty)
cv2.createTrackbar("Sat Max", "Ajustes de Color", 255, 255, empty)
cv2.createTrackbar("Val Min", "Ajustes de Color", 100, 255, empty)
cv2.createTrackbar("Val Max", "Ajustes de Color", 255, 255, empty)

while True:
    # Leer el frame de la webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Leer valores de los sliders
    h_min = cv2.getTrackbarPos("Hue Min", "Ajustes de Color")
    h_max = cv2.getTrackbarPos("Hue Max", "Ajustes de Color")
    s_min = cv2.getTrackbarPos("Sat Min", "Ajustes de Color")
    s_max = cv2.getTrackbarPos("Sat Max", "Ajustes de Color")
    v_min = cv2.getTrackbarPos("Val Min", "Ajustes de Color")
    v_max = cv2.getTrackbarPos("Val Max", "Ajustes de Color")

    # Crear la máscara con los valores seleccionados
    lower_bound = np.array([h_min, s_min, v_min])
    upper_bound = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Aplicar la máscara a la imagen original
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Mostrar la imagen con sliders
    combined_view = np.hstack((frame, result))  # Unir imágenes lado a lado
    cv2.imshow("Ajustes de Color", combined_view)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar ventanas
cap.release()
cv2.destroyAllWindows()
