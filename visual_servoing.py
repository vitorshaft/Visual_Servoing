import cv2
import numpy as np
import serial
drimbot = serial.Serial(port='COM7', baudrate=9600, timeout=.1)


# carrega o classificador em cascata
cascata = cv2.CascadeClassifier('faceRecog.xml')

# define a camera (0 = webcam do pc; 1, 2, 3... = cameras adicionais)
cap = cv2.VideoCapture(1)

# Checa se a webcam foi iniciada corretamente
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    # Le o quadro
    ret, frame = cap.read()
    # print(frame.shape)
    # converte para escala de cinza
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detecta as faces
    faces = cascata.detectMultiScale(cinza, 1.1, 4)
    # desenha retangulo em volta de cada face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        #tamanho = 'X = '+str(x+(w/2))+'Y = '+str(y+(h/2))
        #cv2.putText(frame,tamanho, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0))

        # converte a posicao do rosto em valores das juntas do robo
        j0 = int(180*float(x/640))
        j1 = 179
        j2 = int(180*float(y/480))
        # agrupa os valores das juntas em uma string
        juntas = str(j0)+' '+str(j1)+' '+str(j2)
        # envia a string via serial ao robo
        drimbot.write(bytes(juntas, 'utf-8'))

    # diminui a tela para otimizar processamento
    #frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    # exibe na tela
    cv2.imshow('camera', frame)

    # Interrompe se pressionar ESC
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
