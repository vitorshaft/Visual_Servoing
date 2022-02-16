'''     ANTES DE RODAR O CODIGO CRIE DUAS PASTAS NO MESMO LOCAL DESTE SCRIPT    
    - As pastas devem se chamar 'p' e 'n' (em minúsculo e sem as aspas)
    - A 'p' é para imagens do objeto, em vários angulos e ocupando o maximo da tela possivel
    - A 'n' é para imagens negativas, pode ser tudo que estiver no ambiente, mas não pode
    ter NENHUMA parte do objeto positivo.
'''

import cv2
import numpy as np
from time import sleep

cap = cv2.VideoCapture(1)   #mudar para VideoCapture(0) caso use webcam

while True:
    #previa da camera para apontar corretamente
    #depois de apontar aperte ESC para iniciar
    _, frame = cap.read()

    #Mostra o que a camera enxerga
    cv2.imshow("objeto_alvo", frame)
    key = cv2.waitKey(1)

    if key == 27:        
        break
cv2.destroyWindow("objeto_alvo")
#cria 800 imagens JPG
for i in range(121,800):
    _, frame = cap.read()

    #Mostra oque a camera enxerga
    cv2.imshow("objeto_alvo", frame)
    #mudar o endereco para "/n/..." para imagens negativas
    endereco = "/n/"+str(i)+".jpg"
    print(endereco)
    if _:
        cv2.imwrite(endereco, frame)
    #cv2.destroyWindow("objeto_alvo")
    sleep(0.5)
    #se pressionar ESC ele para
    key = cv2.waitKey(1)

    if key == 27:        
        break

print("amostragem concluida!")