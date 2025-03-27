import cv2

# Capturar la webcam
cap = cv2.VideoCapture(0)

# Leer el primer frame para comparar después
ret, frame1 = cap.read()
frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
frame1 = cv2.GaussianBlur(frame1, (21, 21), 0)  # Suavizado para evitar ruido

while True:
    # Leer el siguiente frame
    ret, frame2 = cap.read()
    if not ret:
        break

    # Convertir a escala de grises y aplicar desenfoque
    gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Calcular la diferencia entre frames
    diff = cv2.absdiff(frame1, gray)

    # Aplicar un umbral para resaltar las áreas con movimiento
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # Mostrar el resultado
    cv2.imshow("Detección de Movimiento", thresh)

    # Actualizar el frame de referencia
    frame1 = gray

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar ventanas
cap.release()
cv2.destroyAllWindows()