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
