import numpy as np
import cv2

# Arbimos la imagen
imagen = cv2.imread(r"/home/lolguin/Desktop/OpenCV/Introduccion/tucan.jpeg",1)
# Espacio de grises
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
# Espacio XYZ
xyz = cv2.cvtColor(imagen, cv2.COLOR_BGR2XYZ)
# Espacio LAB
lab = cv2.cvtColor(imagen, cv2.COLOR_BGR2Lab)
# Espacio HSV
hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

cv2.imshow("Imagen original",imagen)
cv2.imshow("Imagen en gris", grises)
cv2.imshow("Imagen en 1930", xyz)
cv2.imshow("Imagen Lab", lab)
cv2.imshow("Imagen HSV", hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
