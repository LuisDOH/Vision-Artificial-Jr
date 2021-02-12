import numpy as np
import cv2
# Abrir imagen
flores = cv2.imread(r"/home/lolguin/Desktop/OpenCV/Introduccion/Flores_1.jpeg",1)

# Cambiar imagen a escala de grises
copia = cv2.cvtColor(flores,cv2.COLOR_BGR2GRAY)

# Aplicacmos el proceso de umbralizacion
_,umbral = cv2.threshold(copia,200,255,cv2.THRESH_BINARY_INV)

# Segmentar la imagen con color
imagen_final = cv2.bitwise_and(flores, flores, mask = umbral)


# Mostrara la imagen
cv2.imshow("Flores color", flores)
cv2.imshow("Flores gris", copia)
cv2.imshow("Flores Blanco - Negro", umbral)
cv2.imshow("Flores separadas", imagen_final)

cv2.waitKey(0)
cv2.destroyAllWindows()
