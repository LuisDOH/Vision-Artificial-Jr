import cv2
import numpy as np
import imutils

video = cv2.VideoCapture(0)

Fotograma = 0
while True:
    ret, fotogramasVideo = video.read()
    if ret = False:
        print("Fallo la conexion con la camara")
        break

    #Cambiamos el tamanio
    fotogramasVideo = imutils.resize(fotogramasVideo,width = 900)

    # Transformando a grises
    grises = cv2.cvtColor(fotogramasVideo, cv2.COLORBGR2GRAY)

    # Verificamos si los fotogramas sonmayores a 20
    if Fotograma == 20:
        entorno = grises

    if Fotograma > 20:
        diferencias = cv2.absdif(grises, entorno)
        _,umbral = cv2.threshold(diferencias, 50, 255, cv2.THRESH_BINARY)
        lista_contornos, jerarquia = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(fotogramasVideo, lista_contornos, -1, (0,0,255), 3)

        cv2.imshow("diferencias",diferencias)

        for contorno in lista_contornos:
            area = cv2.contourArea(contorno)
            if area > 500:
                 x,y,w,h = cv2.boundingRect(contorno)
                 cv2.rectangle(fotogramasVideo,(x,y),(x+w,y+h),(255,0,255),5)


    cv2.imshow("Imagen", fotogramasVideo)
    Fotograma += 1
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

video.release()
cv2.destroyAllWindows()
