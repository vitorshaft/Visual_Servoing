import cv2
import numpy as np

import serial
drimbot = serial.Serial(port='COM6', baudrate=9600)

#cap = cv2.VideoCapture(0)  #para usar a webcam principal do seu PC
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

while True:
    _, frame = cap.read()
    #cor cinza-escuro
    menor = 20
    maior = 35
    low_cinza = np.array([menor,menor,menor])    #menor RGB possivel
    high_cinza = np.array([maior,maior,maior])   #maior RGB possivel
    cinza_mask = cv2.inRange(frame,low_cinza,high_cinza)    #cria intervalo de cores (mascara)
    contornos, _ = cv2.findContours(cinza_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #procura contornos da cor detectada
    contornos = sorted(contornos, key=lambda x:cv2.contourArea(x), reverse=True)    #inverte a ordem dos contornos
    
    '''Para cada contorno:
        cria regiao retangular ao redor do objeto,
        calcula centro do objeto,
        desenha linha verde no centro do objeto,
        Se o objeto estiver fora do centro (+/- 30 pixels), incrementar ou decrementar motor'''

    for cnt in contornos:
        (x, y, w, h) = cv2.boundingRect(cnt)
        
        x_medio = int((x + x + w) / 2)
        y_medio = int((y + y + h) / 2)
        break
    
    cv2.line(frame, (x_medio, 0), (x_medio, 480), (0, 255, 0), 2)
    cv2.line(frame, (0, y_medio), (320, y_medio), (0,255,0), 2)
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
    # Move servo motor
    if y_medio < centroY -20:
        #posicao += 2
        posicao = 3
    elif y_medio > centro + 20:
        #posicao -= 2
        posicao = 4
    pos = str(posicao)+' '
    drimbot.write(bytes(pos, 'utf-8'))
    '''
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()