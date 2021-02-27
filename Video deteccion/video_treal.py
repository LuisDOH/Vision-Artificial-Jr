import cv2
import numpy as np
import imutils

def Contornos(fotogramas,min,max,area_minima):
    # Conversion a HSV
    hsv = cv2.cvtColor(fotogramas, cv2.COLOR_BGR2HSV)

    # Segmentacion de la imagen
    mascara = cv2.inRange(hsv,min, max)

    # Detectanto contornos a partir de la segmentacion
    lista_contornos, jerarquia = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Ordenar los contornos
    lista_contornos = sorted(lista_contornos, key=cv2.contourArea, reverse=True)

    # Separar los contornos
    contornos_ok = []
    for cada_contorno in lista_contornos:
        area_contorno = len(cada_contorno)
        if area_contorno > area_minima:
            contornos_ok.append(cada_contorno)

    # Ordenar los contornos de mayor a menor solo los que estan como ok
    ord_contornos = sorted(contornos_ok, key=cv2.contourArea, reverse=True)

    # Regresamos la imagen en HSV, la lista de contornos que estan ok
    return (hsv, lista_contornos, ord_contornos)

video = cv2.VideoCapture(0)

while True:
    ret,fotogramasVideo = video.read()
    min = np.array([0,111,229])
    max = np.array([179,255,255])

    hsv,_,contornos = Contornos(fotogramasVideo,min,max,30)
    if len(contornos)>0:
        x,y,w,h = cv2.boundingRect(contornos[0])
        cv2.rectangle(fotogramasVideo,(x,y),(x+w,y+h),(255,0,255),3)
        #cv2.drawContours(fotogramasVideo, contornos, -1, (8,246,255), 1)

    cv2.imshow("Video",fotogramasVideo)
    cv2.imshow("HSV",hsv)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break



video.release()
cv2.destroyAllwindows()
