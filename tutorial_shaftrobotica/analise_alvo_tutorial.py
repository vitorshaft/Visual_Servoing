from cv2 import *
import matplotlib.pyplot as plt

#defina cam_port = 0 para a webcam embutida ou 1,2,3,... para as adicionais
cam_port = 0
cam = VideoCapture(cam_port)

#se der tudo certo, inicializa a camera em modo video
result, image = cam.read()
if result:
    while True:
        _, frame = cam.read()
        #vamos mostrar o que a camera está vendo
        imshow("objeto alvo",frame)

        #depois de posicionar o objeto para tirar foto, apertar 'esc'
        key = waitKey(1)

        if key == 27:
            #quando apertar o 'esc', salva o frame atual em um arquivo de imagem
            imwrite("objeto_alvo.jpg",frame)
            break
    destroyWindow("objeto alvo")

# Se der errado avisa que deu errado kkkk
else:
    print("Deu ruim!")

#Hora de ler a imagem que acabou de ser gerada e ver no que deu:
img = imread("objeto_alvo.jpg",0)
#vamos analisar a partir de seu 'Histograma'

hist = calcHist([img],[0],None,[256],[0,256])

plt.plot(hist)
plt.show()