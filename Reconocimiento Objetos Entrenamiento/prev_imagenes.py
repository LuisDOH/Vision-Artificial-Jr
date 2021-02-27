'''
    @LD-OH =================================================================
        Este modulo servira para redimensionar imagenes (cambiarles
        el tamano) que se utilicen para el entrenamiento de un modelo.
        Ya que entre mas grande la magen mayor tiempo tarda en procesar
        y entrenar la red. Ademas algunos metodos de entrenamiento como
        el que se usara en esta practica requieren que las imagenes de
        entrenamiento tengan el mismo tamano.
    ========================================================================
'''

from multiprocessing import Pool
import os
import cv2



# Solicitamos la ruta de la carpeta donde estan las imagenes que queremos
# redimensionar
directorio = r""
# A que tamano se quieren redimensionar
ancho = 60
alto = 60

# Verificamos si es valida la carpeta que contiene las imagenes
try:
    lista_fotos = os.listdir(directorio)
    print(f"Esta carpeta contiene: {len(lista_fotos)} imagenes")
except:
    print("")
    print("")
    print("No fue posible leer las imaganes de la carpeta")
    print("======== CIERRE DEL PROGRAMA =========")
    print("")
    exit()

print("Comienza el proceso de redimension")

for foto in lista_fotos:
    imagen = cv2.imread(f"{directorio}\{foto}",1)
    redim = cv2.resize(imagen, (ancho, alto))
    cv2.imwrite(f"\{foto}", redim)

print("====== Fin del programa =====")
