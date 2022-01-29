from cv2 import *
import matplotlib.pyplot as plt

#defina cam_port com: 0 - camera principal do PC; 1, 2, 3, ... - cameras adicionais (USB)
cam_port = 1
cam = VideoCapture(cam_port)

# tenta ler uma imagem pela camera
result, image = cam.read()

#se der tudo certo, inicializa a camera em modo video
if result:
    while True:
        _, frame = cam.read()

        #Mostra oq ue a camera enxerga
        imshow("objeto_alvo", frame)

        #aguarda pressionar 'ESC' (codigo 27 ali)
        key = waitKey(1)

        if key == 27:
            #salva frame atual com o nome de "objeto_alvi.png"
            imwrite("objeto_alvo.png", frame)
            break
    destroyWindow("objeto_alvo")

# Se der algo errado, exibe essa mensagem
else:
    print("Nenhuma imagem detectada. Tente novamente!")

#Le imagem que acabou de ser criada
img = imread("objeto_alvo.png",0)
#exibe histograma da imagem (valor RGB/quantidade de pixels)
histg = calcHist([img],[0],None,[256],[0,256])

plt.plot(histg)
plt.show()