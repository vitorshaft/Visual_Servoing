import cv2
import numpy as np
import serial

drimbot = serial.Serial(port='COM7',baudrate=9600)

cap = cv2.VideoCapture(1)

#configura resolução da camera
# 3 é a largura e 4 é a altura do frame
cap.set(3,480)
cap.set(4,320)

#analisa amostra da imagem
_, frame = cap.read()
linhas, cols, _ = frame.shape   #obtem numero de linhas e colunas da imagem
x_medio = int(cols/2)   #calcula x do meio da tela (vai mudar)
centro = int(cols/2)    #essa variavel vai permanecer
posicao = 90            #robo vai começar an posição 90 graus

while True:
    _, frame = cap.read()
    #aqui vamos definir a cor que queremos rastrear
    menor = np.array([10,10,10])    #RGB menor
    maior = np.array([40,40,40])    #RGB maior
    mascara = cv2.inRange(frame,menor,maior) #cria intervalo de cores
    #procura contornos da cor desejada
    contornos, _ = cv2.findContours(mascara,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #reordena lista de contornos encontrados começando com a MAIOR ÁREA (maior objeto)
    contornos = sorted(contornos,key=lambda x:cv2.contourArea(x), reverse=True)

    for cnt in contornos:
        (x,y,w,h) = cv2.boundingRect(cnt)
        x_medio = int((x+x+w)/2)
        break
    cv2.line(frame,(x_medio,0),(x_medio,480),(0,255,0),2)

    #hora de mover o servo-motor
    if x_medio < centro-30:
        posicao +=2
    elif x_medio > centro+30:
        posicao -=2
    pos = str(posicao)+' '
    drimbot.write(bytes(pos,'utf-8'))

    cv2.line(frame, (x_medio,0),(x_medio,480),(0,255,0),2)

    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()