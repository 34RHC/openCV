import cv2
import numpy as np

# Función vacía para los trackbars
def empty(a):
    pass

# Captura de la webcam
cap = cv2.VideoCapture(0)

# Crear ventana con los sliders
cv2.namedWindow("Ajustes")
cv2.createTrackbar("Hue Min", "Ajustes", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Ajustes", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Ajustes", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Ajustes", 255, 255, empty)
cv2.createTrackbar("Val Min", "Ajustes", 0, 255, empty)
cv2.createTrackbar("Val Max", "Ajustes", 255, 255, empty)

while True:
    # Leer el frame de la cámara
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Leer valores de los sliders
    h_min = cv2.getTrackbarPos("Hue Min", "Ajustes")
    h_max = cv2.getTrackbarPos("Hue Max", "Ajustes")
    s_min = cv2.getTrackbarPos("Sat Min", "Ajustes")
    s_max = cv2.getTrackbarPos("Sat Max", "Ajustes")
    v_min = cv2.getTrackbarPos("Val Min", "Ajustes")
    v_max = cv2.getTrackbarPos("Val Max", "Ajustes")

    # Crear la máscara
    lower_bound = np.array([h_min, s_min, v_min])
    upper_bound = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Aplicar la máscara a la imagen original
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Mostrar ventanas
    cv2.imshow("Imagen Original", frame)
    cv2.imshow("Máscara", mask)
    cv2.imshow("Resultado", result)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()


