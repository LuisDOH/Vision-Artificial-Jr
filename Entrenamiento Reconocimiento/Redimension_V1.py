'''
    @LD-OH ============================================================================================================
        Este modulo servira para redimensionar (cambiarles el tamaño) imagenes que se usaran para el entrenamiento
        de un modelo de reconocmiento.
        
        Entre mas grande sean las imagenes de entregamiento, mayor sera el tiempo que tarde en entrenar la red neuronal. 
        Ademas algunos metodos de entrenamiento como el que se usara en esta practica requieren que las imagenes de
        entrenamiento tengan el mismo tamaño, tanto las positivas (donse esta el objeto que queremos detectar) como las
        negativas (aquellas donde no aparece nuestro objeto a detectar).

        Cuando se dispone de muy poca informacion (pocas imagenes) para el entrenamiento de un modelo, se suelen
        generar imagenes estirando, rotando, difuminando o volteando la imagen original, para generar nueva informacion
        a partir de la informacion que ya se tiene. No es tan efectivo como agregar mas imagenes nuevas del objeto
        pero suele ser mejor que nada.

        * Entre mas informacion le des al modelo de entremiento, mejor sera el aprendizaje de la red neuronal
    ====================================================================================================================
'''

# Importamos las librerias necesarias para el programa
import os
from PIL import Image

# Solicitamos la ruta de la carpeta donde estan nuestras fotos y el ancho y alto en pixeles que queremos obtener
directorio = input("Arrastre la carpeta con las imagenes que desea redimensionar: ")
ancho      = int(input("Ingrese el ancho deseado en pixeles: "))
alto       = int(input("Ingrese el alto deseado en pixeles: "))

# Le preguntamos al usuario si desea utilizar la funcion de rotar imagenes, para crear mas informacion  a partir de la que ya se tiene
# Esto significa que ademas de la foto redimensionada, agregara dos fotos mas, una girada 90 grados y otro girada 180
while True:
    rotacion = int(input("Desea generar imagenes rotadas para incrementar un poco mas los datos para entrenamiento (1 = SI / 2 = NO): "))
    if(rotacion == 1 or rotacion == 2):
        break
    else:
        print("Elija una de las opciones correctas 1 = SI/ 2 = NO")

# Quitamos algunas comillas extras que se agregan automaticamente cuando solicitamos la ruta usando input
directorio = directorio.strip('"')

# Creamos una estructura de control de errores, si el sistema no puede leer la carpeta el programa se detiene
try:
    print("\n\n")
    lista_fotos = os.listdir(directorio)
    # lista_fotos solo guarda en una lista el nombre de todas las fotos que encontro en la carpeta
except:
    print("\nNo se ha podido leer correctamente la carpeta!!!")
    print("======== Fin del programa ==========\n")
    exit()

# Creamos una carpeta llamada "procesadas", donde se guardaran las imagenes con el nuevo tamaño
if not os.path.exists(f"{directorio}\procesadas"):
        os.makedirs(f"{directorio}\procesadas")

# Comenzamos el proceso, creamos un comntador que cuente las imagenes que se han generado
print("Comienza el proceso de re-dimension de imagenes\n")
contador = 0

# Recorremos todas las imagenes que estan dentro de la carpeta
for foto in lista_fotos:
    #   Abrimos cada una de las fotos usando la funcion Image.open() de la libreria PIL, le indicamos la direccion de la carpera y el nombre 
    # de la foto con f"{directorio}\{foto}"
    imagen = Image.open(f"{directorio}\{foto}")
    print(f"{imagen.format} -- dimensiones: {imagen.size} ==> {ancho}x{alto} px")

    # Cambiamos el tramaño de la imagen con el ancho y el alto que introducimos por consola
    redinmension = imagen.resize((ancho, alto))
    # Guardamos la imagen con el nuevo tamaño e incrementamos el contador
    redinmension.save(fr"{directorio}\procesadas\{foto}")
    contador += 1
    
    # Si el usuario eligio 1 (SI al proceso de rotacion), creamos dos imagenes mas, las cuales estan rotada 90 y 180 grados
    # Y las guardamos en nuestra carpeta de "procesadas" agregando un prefijo rotada90_ o rotada180_.
    if(rotacion == 1):
        imagen90  = redinmension.rotate(90)
        imagen180 = redinmension.rotate(180)
        imagen90.save(fr"{directorio}\procesadas\rotada90_{foto}")
        imagen180.save(fr"{directorio}\procesadas\rotada180_{foto}")
        contador += 2

        #Limpiamos la ram eliminando las variables que creamos para las imagenes, esto ayuda a liberar parte de la memoria usada
        del(imagen90)
        del(imagen180)

    del(imagen)
    del(redinmension)
   

print(f"\n\n====== Proceso Terminado ==========")
print(f"Total de imagenes generadas: {contador}")