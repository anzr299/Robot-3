import cv2
import sys
import serial
import io
import pyttsx



engine = pyttsx.init()
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_no = 0
video_capture = cv2.VideoCapture(0)
img = cv2.imread('emoji.jpeg',1)
img1 = cv2.imread('emoji1.png',1)
ser = serial.Serial("/dev/ttyACM0" ,9600)
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

    if len(faces) > 0 :      
        ser.write('0') 
            

    elif len(faces) == 0:
        face_no += 1
        if face_no > 2:
            print "No Faces"
            ser.write('1')

    
    if ser.read() == '2':
        print "face found!"
        engine.say("Hello world")
        cv2.imshow('emoji' , img)

            
					


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
