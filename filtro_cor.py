import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read()
    #hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #cor selecionada
    menor = 18
    maior = 100
    low_red = np.array([menor,menor,menor])
    high_red = np.array([maior,maior,maior])
    #red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red_mask = cv2.inRange(frame,low_red,high_red)

    cv2.imshow("Normal",frame)
    cv2.imshow("Filtrada",red_mask)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()