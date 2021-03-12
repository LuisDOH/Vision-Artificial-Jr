import cv2
import numpy as np
import imutils


video = cv2.VideoCapture(r"C:\Users\Luis David\Desktop\reconocimiento objeto\VID_20210226_141244.mp4")
clasificador = cv2.CascadeClassifier(r"D:\Personal\StepAcademy\Inteligencia Artificial Jr 5\Reconocimiento de objetos CV\Redimension\Entrenamiento\classifier\cascade.xml")

while(video.isOpened()):
    ret, fotograma = video.read()
    fotograma = imutils.resize(fotograma,width = 500)
    grises = cv2.cvtColor(fotograma, cv2.COLOR_BGR2GRAY) 

    objetivo = clasificador.detectMultiScale(grises, scaleFactor = 1.3, minNeighbors = 50, minSize=(150,150), maxSize=(200,200))
    
    for (x,y,w,h) in objetivo:
        cv2.rectangle(fotograma, (x,y,x+w,y+h), (0,0,255),2)

    cv2.imshow("Video", fotograma)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
