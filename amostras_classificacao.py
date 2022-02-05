import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read()

    #Mostra o que a camera enxerga
    cv2.imshow("objeto_alvo", frame)
    key = cv2.waitKey(1)

    if key == 27:        
        break
cv2.destroyWindow("objeto_alvo")

for i in range(200):
    _, frame = cap.read()

    #Mostra oq ue a camera enxerga
    cv2.imshow("objeto_alvo", frame)
    cv2.imwrite("/p/1.jpg", frame)
    #aguarda pressionar 'ESC' (codigo 27 ali)
    key = cv2.waitKey(1)

    if key == 27:        
        break
cv2.destroyWindow("objeto_alvo")
print("amostragem concluida!")