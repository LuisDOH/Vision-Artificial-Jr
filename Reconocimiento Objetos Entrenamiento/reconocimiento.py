import cv2
import numpy as np
import imutils

video = cv2.VideoCapture(r"")
clasificador = cv2.CascadeClassifier(r'')


while (video.isOpened()):
    ret, fotogramasVideo = video.read()
    fotogramasVideo = imutils.resize(fotogramasVideo,width = 500)
    grises = cv2.cvtColor(fotogramasVideo, cv2.COLOR_BGR2GRAY)


    objetivo = clasificador.detectMultiScale(grises,
    scaleFactor = 3.5,
    minNeighbors = 50,
    minSize=(100,100),
    maxSize=(300,300))

    for (x,y,w,h) in objetivo:
        cv2.rectangle(fotogramasVideo, (x,y,x+w,y+h), (0,0,255),2)


    cv2.imshow("Video", fotogramasVideo)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break


video.release()
cv2.destroyAllWindows()
