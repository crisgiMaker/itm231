import cv2
import numpy as np
import RPi.GPIO as GPIO
import time

# Inicializar GPIO para controlar el brazo robótico y los LEDs
GPIO.setmode(GPIO.BCM)



led_green_pin = 22
led_yellow_pin = 23


GPIO.setup(led_green_pin, GPIO.OUT)
GPIO.setup(led_yellow_pin, GPIO.OUT)




# Función para detectar la madurez de la fruta
def detect_fruit_ripeness(frame):
    # Convertir la imagen a espacio de color HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Definir los rangos de color para detectar frutas inmaduras (verde)
    lower_green = np.array([25, 50, 50])
    upper_green = np.array([75, 255, 255])

    # Definir los rangos de color para detectar frutas maduras (amarillo)
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    # Crear máscaras para detectar los colores
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Encontrar contornos para frutas verdes
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Encontrar contornos para frutas amarillas
    contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Determinar si hay frutas maduras o inmaduras
    if len(contours_yellow) > 0:
        print("La fruta está madura")
        GPIO.output(led_yellow_pin, GPIO.HIGH)
        GPIO.output(led_green_pin, GPIO.LOW)
    elif len(contours_green) > 0:
        print("La fruta está inmadura")
        GPIO.output(led_green_pin, GPIO.HIGH)
        GPIO.output(led_yellow_pin, GPIO.LOW)
    else:
        GPIO.output(led_green_pin, GPIO.LOW)
        GPIO.output(led_yellow_pin, GPIO.LOW)

    # Devolver las máscaras para visualización
    return mask_green, mask_yellow

# Capturar video de la cámara
cap = cv2.VideoCapture(0)

try:
    while True:
        # Leer un fotograma del video
        ret, frame = cap.read()

        if not ret:
            break

        # Detectar madurez de las frutas
        mask_green, mask_yellow = detect_fruit_ripeness(frame)

        # Mostrar la imagen original y las máscaras
        cv2.imshow('Original', frame)
        cv2.imshow('Mask - Green', mask_green)
        cv2.imshow('Mask - Yellow', mask_yellow)

        # Salir del bucle al presionar 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Limpiar y cerrar
    cap.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()
