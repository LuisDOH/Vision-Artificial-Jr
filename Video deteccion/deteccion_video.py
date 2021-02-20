import cv2
import numpy as np
import imutils

video = cv2.VideoCapture(f"/home/lolguin/Desktop/ItStep/Junior 5/Pre-clase/OpenCV/Filtros/Vdrone.mp4")

while (video.isOpened()):
    ret, fotogramasVideo = video.read()
    fotogramasVideo = imutils.resize(fotogramasVideo,width = 800)

    hsv = cv2.cvtColor(fotogramasVideo, cv2.COLOR_BGR2HSV)

    min = np.array([84,158,87])
    max = np.array([120,235,255])

    mascara = cv2.inRange(hsv,min, max)
    contornos, jerarquia = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    ord_contornos = sorted(contornos, key=cv2.contourArea, reverse=True)

    cv2.drawContours(fotogramasVideo, contornos, -1, (0,255,0), 3)

    contornos_ok = []
    for i in contornos:
        if len(i)>60:
            contornos_ok.append(i)

    cv2.drawContours(fotogramasVideo, contornos_ok, -1, (0,0,255), 3)
    
    cv2.imshow("Video", fotogramasVideo)
    cv2.imshow("HSV", hsv)

    del (contornos, contornos_ok)

    if (cv2.waitKey(15) & 0xFF == ord('q')):
        break

video.release()
cv2.destroyAllWindows()
