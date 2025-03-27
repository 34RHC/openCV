import cv2

# Capturar vídeo desde la cámara
cap = cv2.VideoCapture(0)  # 0 indica la webcam principal

while True:
    ret, frame = cap.read()  # Leer frame de la cámara
    if not ret:
        break  # Salir si hay error

    cv2.imshow('Webcam', frame)  # Mostrar frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Salir con tecla 'q'
        break

cap.release()
cv2.destroyAllWindows()