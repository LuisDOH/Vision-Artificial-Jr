'''
@LD-OLGUIN===================================================================================================================================================
    Este Script experimentaremos con algunos filtros para tratar de remover la interferencia de la imagen de un zorro
==============================================================================================================================================================
'''

import numpy as np
import cv2

# Importar la imagen del zorro
fox = cv2.imread(r"/home/lolguin/Desktop/OpenCV/Introduccion/zorro.png",0)

# Creamos una copia (recomendable para no afectar la imagen original)
copia = fox

# Filtro de gauss
gauss = cv2.GaussianBlur(copia,(13,13),23)

# Filtro de Mediana
mediana = cv2.medianBlur(copia,3)



cv2.imshow("fox", copia)
cv2.imshow("fox-gauss", gauss)
cv2.imshow("Fox-mediana",mediana)
cv2.waitKey(0)
