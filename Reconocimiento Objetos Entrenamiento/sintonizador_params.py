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
    cv2.namedWindow("Parametros Reconocimiento")
    # Creamos las barritas para los valores
    cv2.createTrackbar("scaleFactor","Parametros Reconocimiento",10,10,nada)
    cv2.createTrackbar("minNeighbors","Parametros Reconocimiento",255,255,nada)
    cv2.createTrackbar("minSize","Parametros Reconocimiento",1000,1000,nada)
    cv2.createTrackbar("maxSize","Parametros Reconocimiento",100,1000,nada)


def valores_deteccion():
    #Posicionamos la barra
    sFactor    = cv2.getTrackbarPos("scaleFactor","Parametros Reconocimiento")
    mNeighbors = cv2.getTrackbarPos("minNeighbors","Parametros Reconocimiento")
    mS         = cv2.getTrackbarPos("minSize","Parametros Reconocimiento")
    mxS        = cv2.getTrackbarPos("maxSize","Parametros Reconocimiento")

    v_parametros = (sFactor,mNeighbors,mS,mxS)
    return v_parametros

crear_barras()

while True:

    # Importamos la imagen
    fotografia = cv2.imread(r"D:\Personal\StepAcademy\Inteligencia Artificial Jr 5\Reconocimiento de objetos CV\positivo\IMG_20210226_112617.jpg",1)
    fotografia = imutils.resize(fotografia,width = 800)
    clasificador = cv2.CascadeClassifier(r'C:\Users\Luis David\Desktop\reconocimiento objeto\cascade.xml')

    # Cambiamos el espacio de la imagen
    grises = cv2.cvtColor(fotografia, cv2.COLOR_BGR2GRAY)


    # Ejecutamos nuestra funcion
    scale, neighbors, min, max = valores_deteccion()

    objetivo = clasificador.detectMultiScale(grises,
    scaleFactor = scale,
    minNeighbors = neighbors,
    minSize=(min,min),
    maxSize=(max,max))

    for (x,y,w,h) in objetivo:
        cv2.rectangle(fotografia, (x,y,x+w,y+h), (0,0,255),2)

    cv2.imshow("Video", fotografia)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
