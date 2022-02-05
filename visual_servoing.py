import cv2
import numpy as np
import serial
drimbot = serial.Serial(port='COM6', baudrate=9600)


# carrega o classificador em cascata
cascata = cv2.CascadeClassifier('cascade.xml')

# define a camera (0 = webcam do pc; 1, 2, 3... = cameras adicionais)
cap = cv2.VideoCapture(1)

# Configura resolucao da camera
cap.set(3, 480)     #largura
cap.set(4, 320)     #altura

#analisa uma amostra da imagem
_, frame = cap.read()
linhas, cols, _ = frame.shape   #obtem numero de linhas e colunas da imagem
x_medio = int(cols / 2)         #calcula x do meio da tela
y_medio = int(linhas/2)         #calcula y do meio da tela
centro = int(cols / 2)          #mesma coisa, mas essa variavel nao vai mudar
centroY = int(linhas/2)         
posicao = 90 # degrees          #valor inicial do motor do robo

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
    faces = cascata.detectMultiScale(cinza, 1.1, 25,None,[50,50])
    # desenha retangulo em volta de cada face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        x_medio = int((x + x + w) / 2)
        y_medio = int((y + y + h) / 2)
        break
    cv2.line(frame, (x_medio, 0), (x_medio, 480), (0, 255, 0), 2)
    # converte a posicao do rosto em valores das juntas do robo
    # Move servo motor
    if x_medio < centro -30:
        #posicao += 2
        posicao = 1
    elif x_medio > centro + 30:
        #posicao -= 2
        posicao = 2
    pos = str(posicao)+' '
    drimbot.write(bytes(pos, 'utf-8'))
    '''
    j0 = int(180*float(x/640))
    j1 = 179
    j2 = int(180*float(y/480))
    # agrupa os valores das juntas em uma string
    juntas = str(j0)+' '+str(j1)+' '+str(j2)
    # envia a string via serial ao robo
    drimbot.write(bytes(juntas, 'utf-8'))
    '''

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
