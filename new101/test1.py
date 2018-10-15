import cv2
import sys
import io
import pyttsx


count = 0
a = "n"
b = False
engine = pyttsx.init()
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)
img = cv2.imread('emoji.jpeg',1)
img1 = cv2.imread('emoji1.png',1)
while True:
    cv2.imshow('emoji', img1)
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(40, 40),
    )

    while len(faces) > 0:
        b = True
        a = "y"
        cv2.imshow('emoji', img1)
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(40, 40),

        
    )

    if b == True:
        print "face detected"

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()