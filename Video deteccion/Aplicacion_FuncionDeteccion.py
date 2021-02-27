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



video = cv2.VideoCapture(f"/home/lolguin/Desktop/ItStep/Junior 5/Pre-clase/OpenCV/Filtros/Vdrone.mp4")

while (video.isOpened()):
    ret, fotogramasVideo = video.read()
    fotogramasVideo = imutils.resize(fotogramasVideo,width = 800)

    min = np.array([84,158,87])
    max = np.array([120,235,255])

    hsv, contronos, contornos_ok = Contornos(fotogramasVideo, min,max,50)
    #cv2.drawContours(fotogramasVideo, contornos_ok, -1, (0,255,0), 3)

    if len(contornos_ok)>0:
        x,y,w,h = cv2.boundingRect(contornos_ok[0])
        cv2.rectangle(fotogramasVideo,(x,y),(x+w,y+h),(255,0,255),3)


    cv2.imshow("Original", fotogramasVideo)
    cv2.imshow("HSV", hsv)

    if (cv2.waitKey(15) & 0xFF == ord('q')):
        break

video.release()
cv2.destroyAllWindows()
