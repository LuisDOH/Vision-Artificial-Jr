import numpy as np
import cv2

# Importar imagen
abeja = cv2.imread(r"/home/lolguin/Desktop/OpenCV/Introduccion/abeja.jpeg",1)

# Tranformamos a HSV
hsv = cv2.cvtColor(abeja, cv2.COLOR_BGR2HSV)

# Min de color
min_color = np.array([0,0,143])
# Max de color
max_color = np.array([179,255,255])

# Separar la imagen con los valores que encontramos
abeja_separada =  cv2.inRange(hsv,min_color, max_color)

# Imagen Final
abeja_final = cv2.bitwise_and(abeja, abeja, mask = abeja_separada)

#Mostar imagen
cv2.imshow("Original", abeja)
cv2.imshow("HSV", hsv)
# Imagen que separamos por el rango de color
cv2.imshow("Abeja separada", abeja_separada)
# Imagen abeja_final
cv2.imshow("Imagen final", abeja_final)
cv2.waitKey(0)
cv2.destroyAllWindows()
