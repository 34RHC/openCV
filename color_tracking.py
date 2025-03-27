import cv2
import numpy as np

# Capturar la webcam
cap = cv2.VideoCapture(1)

# Definir el rango de color en HSV (Azul en este caso)
lower_blue = np.array([100, 150, 50])  # Límite inferior
upper_blue = np.array([140, 255, 255])  # Límite superior

while True:
    # Leer el frame de la webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir a espacio de color HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Crear una máscara para detectar el color azul
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Encontrar contornos en la máscara
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar los contornos en la imagen original
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Filtrar objetos pequeños
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Rectángulo verde

    # Mostrar la imagen con el seguimiento
    cv2.imshow("Seguimiento de Color", frame)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar ventanas
cap.release()
cv2.destroyAllWindows()
