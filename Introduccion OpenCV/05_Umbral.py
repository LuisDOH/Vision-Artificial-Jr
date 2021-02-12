'''
@LD-OLGUIN===================================================================================================================================================
    Este Script se muestran los umbrales principales para hacer segmentacion. Una umbralizacion consiste en establecer un valor en escala de 
    grises a partir del cual, los valores de esten por debajo de ese numero se convertiran en cero y los que sean iguales o superiores a ese 
    valor se convertiran en 255.
    
        * Recortar que en una imagen en escala de grises 
            0   => oscuridad total (No hay color)
            255 => luz total (blanco) "Equivalente a 1 en binario"
    
    _,imagen_resultado = cv2.threshold(imagen,Umbral,255, Tipo_de_Umbral) => Esta funcion nos permite aplicar un humbral 

    Tipos de umbrales
    cv2.THRESH_BINARY     -> Valores por encima o iguales al umbral => 255; Valores inferiores al umbral => 0
    cv2.THRESH_BINARY_INV -> Similar al anterior pero alreves, valores superiores o iguales al umbral =>0; valores inferiores al umbral => 255

    * Mas informacion sobre los Umbrales:
        https://omes-va.com/simple-thresholding/

==============================================================================================================================================================
'''

import numpy as np
import cv2
# Libreria para redimensionar nuestras imagenes
import imutils

flor = cv2.imread(r"/home/lolguin/Desktop/OpenCV/Introduccion/Flores_1.jpeg",1)
# Redimensionamos nuestra imagen
flor = imutils.resize(flor,width = 400)

# Obtenemos una copia
copia = cv2.cvtColor(flor,cv2.COLOR_BGR2GRAY)


# Umbral Sencillo
[_,umbralBinario] = cv2.threshold(copia,160,255,cv2.THRESH_BINARY_INV)

# La funcion bitwise explicada en clase permite hacer operaciones binarias entre las imagenes para aplicar color en una region
# o remover el color de esa region
ImagenFiltrada = cv2.bitwise_and(flor,flor, mask = umbralBinario)

cv2.imshow("Original", flor)
cv2.imshow("Gris",copia)
cv2.imshow("Umbral binario",umbralBinario)
cv2.imshow("Final",ImagenFiltrada)
cv2.waitKey(0)
