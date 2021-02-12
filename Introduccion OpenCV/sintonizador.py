import numpy as np
import cv2
# Libreria para redimensionar nuestras imagenes
import imutils

# ======== FUNCION PARA CREAR BARRA DE COLOR ===============
def nada(x):
    # Esta funcion no sirve para nada pero la necesitamos para
    # que funcione nuestro programa
    pass


def crear_barras():
    # Creamos una ventana
    cv2.namedWindow("Barra espacio HSV")
    # Creamos las barritas para los minimos
    cv2.createTrackbar("L-H","Barra espacio HSV",0,179,nada)
    cv2.createTrackbar("L-S","Barra espacio HSV",0,255,nada)
    cv2.createTrackbar("L-V","Barra espacio HSV",0,255,nada)

    # Creamos las barritas para los maximos
    cv2.createTrackbar("H-H","Barra espacio HSV",179,179,nada)
    cv2.createTrackbar("H-S","Barra espacio HSV",255,255,nada)
    cv2.createTrackbar("H-V","Barra espacio HSV",255,255,nada)


def valores_HSV():
    #Posicionamos la barra
    min_h = cv2.getTrackbarPos("L-H","Barra espacio HSV")
    min_s = cv2.getTrackbarPos("L-S","Barra espacio HSV")
    min_v = cv2.getTrackbarPos("L-V","Barra espacio HSV")

    max_h = cv2.getTrackbarPos("H-H","Barra espacio HSV")
    max_s = cv2.getTrackbarPos("H-S","Barra espacio HSV")
    max_v = cv2.getTrackbarPos("H-V","Barra espacio HSV")

    v_min = np.array([min_h,min_s,min_v])
    v_max = np.array([max_h,max_s,max_v])
    return [v_min, v_max]

# Importamos la imagen
fotografia = cv2.imread(r"/home/lolguin/Desktop/OpenCV/Introduccion/abeja.jpeg",1)
fotografia = imutils.resize(fotografia,width = 400)

# Cambiamos el espacio de la imagen
foto_hsv = cv2.cvtColor(fotografia, cv2.COLOR_BGR2HSV)

crear_barras()

while True:
    # Ejecutamos nuestra funcion
    [min, max] = valores_HSV()

    # Creamos una mascara para detectar el color que buscamos
    mascara_deteccion = cv2.inRange(foto_hsv, min, max)

    # Mostramos la imagen
    cv2.imshow("Imagen Normal", fotografia)
    cv2.imshow("Imagen HSV", foto_hsv)
    cv2.imshow("Sintonizar", mascara_deteccion)

    # Estructura para cierre de la ventana
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
