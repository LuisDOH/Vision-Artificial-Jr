'''
@LD-OLGUIN===================================================================================================================================================
    Este Script muestra como seleccionar una area especifica de la imagen y reposicionarla en otra region

        * Recordar que para una maquina, una imagen es interpretada como una matriz de numeros, es decir un arreglo de numeros que regresenta
          los valores RGB (RED,GREEN, BLUE) de cada pixel en la foto. Cade pizel contendra entonces informacion del tipo  [[255,87,22]] =>[RGB]

        *  Recordar que openCV lee los valores de RGB alreves, es decir RGB => BGR (Los lee como BLUE, GREEN, RED)

        * Si seleccionamos una region en lugar de un pixel la informacion es convertida a un tensor (un arreglo de tres dimensiones), que se 
          vera de la siguient forma (100, 100, 3) => (ancho en x, altura en y, capas de color).
    
    Ya que la imagen es un conjunto de numeros, podemos decirle a Python que selecciones una region especifica y esta region la podemos separar,
    exportar o reposicionarla en la imagen original.

==============================================================================================================================================================
'''


import numpy as np
import cv2

foto = cv2.imread("/home/lolguin/Desktop/ItStep/Junior 5/Pre-clase/OpenCV/Introduccion/tucan.jpeg",1)

# Seleccionamos un area [x_inicio, x_fin, y_inicio,y_fin]
area = foto[100:200,100:200]

# Mostramos la matriz de pixeles del area seleccionada 
print(area)
cv2.imshow("corte",area)

# Esperamos una tecla para realizar el siguiente paso
cv2.waitKey(0)

# Cuando introducimos en dos dimensiones el area nos da la posicion
#el tercer elemento nos da los valores de la capa que seleccionamos
# 0 B, 1 G, 2 R
#area = foto[100:200,100:200,1]
#print(area)
#print(area.shape)
#cv2.imshow("corte",area)
#cv2.waitKey(0)

# Abrimos una imagen
foto1 = cv2.imread("/home/lolguin/Desktop/ItStep/Junior 5/Pre-clase/OpenCV/Introduccion/tucan.jpeg",1)

# Seleccionamos el area de interes [x_inicio, x_fin, y_inicio,y_fin]
recorte = foto1[100:200,100:200]

# Imprimimos las dimensiones del area que seleccionamos (ancho, alto, capas de color)
print(recorte.shape)
cv2.imshow("Recorte", recorte)
cv2.waitKey(0)

# Reposicionamos el recorte en otra seccion de la imagen original
foto1[250:350, 300:400] = recorte
cv2.imshow("Reposicionamiento",foto1)
cv2.waitKey(0)

# Para ir borrando colores de las capas de mi imagen
# Se divide la imagen en los colores
[b,g,r] = cv2.split(foto1)

# Mostramos solo la capa roja (Ojo no se vera roja se vera en escala de grises
# Entre mas oscuro es el gris mas color rojo hay en esa region)
cv2.imshow('Capa roja', r)
cv2.waitKey(0)

# Podemos quitar el color rojo de la imagen cambiando todos los valores de la capa roja a cero
for index in range(len(r)):
    r[index] = 0

# Para unir de nueva todas las capas de color
imagen_reformada = cv2.merge((b,g,r))
cv2.imshow("Imagen recuperada",imagen_reformada)
cv2.waitKey(0)


