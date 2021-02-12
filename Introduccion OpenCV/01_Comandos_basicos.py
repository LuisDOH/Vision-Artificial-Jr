'''
@LD-OLGUIN===================================================================================================================================================
    Aqui se muestra el uso de los tres comando basicos para abrir, 
    mostrar y guardar una imagen con openCV

    cv2.imread("direccion\de\archivo", modo)                                => leer imagen desde archivo
    cv2.imshow("titulo de la ventana", variable donde se guarda la ventana) => mostrar imagen 
    cv2.imwrite("direccion\de\guardado", variabledeImagen)                  => guardar imagen

    cv2.waitKey(0)          => Esperamos una tecla para cerrar ventanas
    cv2.destroyAllWindows   => Destruimos todas las ventanas para limpiar ram  

    modos de apertura de imagen
    0  => Escala de grises
    1  => A color
    -1 => Imagen PNG sin fondo
==============================================================================================================================================================
'''
import cv2
import numpy

# Importamos imagenes
foto = cv2.imread("/home/lolguin/Desktop/ItStep/Junior 5/Pre-clase/OpenCV/Introduccion/tucan.jpeg",0)
# Mostramos imagenes
cv2.imshow('image',foto)
# Esperamos tecla
cv2.waitKey(0)
# Guardamos imagen
cv2.imwrite('/home/lolguin/Desktop/ItStep/Junior 5/Pre-clase/OpenCV/Introduccion/endgame.png',foto)
# Destruimos ventanas
cv2.destroyAllWindows()
