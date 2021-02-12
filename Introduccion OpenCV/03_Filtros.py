'''
@LD-OLGUIN===================================================================================================================================================
    Este Script se abordan los filtros mas sencillos pero utiles disponibles en openCV
    Un filtro es una operacion matematica que se le aplica al valor de los pixeles de una imagen para recuperar informacion perdida por ruido en la imagen
    o para resaltar informacion de interes.

    * Los filtros descritos acontinuacion se aplican a imagenes en escala de grises

==============================================================================================================================================================
'''

import numpy as np
import cv2

# importar nuestra imagen
fotografia = cv2.imread(r"/home/lolguin/Desktop/OpenCV/Introduccion/tucan.jpeg",1)

copia = fotografia

# Filtro Gaussiano
gauss = cv2.GaussianBlur(copia,(9,7),151)

# Filtro de mediana
mediana = cv2.medianBlur(copia,35)

#  Filtro Bilateral
bilateral = cv2.bilateralFilter(copia,9,75,75)

# Msstramos las imagenes obtenidas con los filtros
cv2.imshow("Tucan",fotografia)
cv2.imshow("Tucan-gauss",gauss)
cv2.imshow("Tucan-Mediana", mediana)
cv2.imshow("Tucan-Bilateral",bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
