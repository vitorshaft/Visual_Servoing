import cv2
import numpy as np

import serial
drimbot = serial.Serial(port='COM7', baudrate=9600)

cap = cv2.VideoCapture(1)

# Configura resolucao da camera
cap.set(3, 480)
cap.set(4, 320)

_, frame = cap.read()
rows, cols, _ = frame.shape
x_medium = int(cols / 2)
center = int(cols / 2)
position = 90 # degrees

while True:
    _, frame = cap.read()
    hsv_frame = frame
    #cor cinza-escuro
    #low_cinza = np.array([0,0,5])
    #high_red = np.array([0,0,100])
    low_cinza = np.array([15,15,15])
    high_cinza = np.array([50,50,50])
    cinza_mask = cv2.inRange(hsv_frame,low_cinza,high_cinza)
    contours, _ = cv2.findContours(cinza_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        
        x_medium = int((x + x + w) / 2)
        break
    
    cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
    # Move servo motor
    if x_medium < center -30:
        position += 1
    elif x_medium > center + 30:
        position -= 1
    pos = str(position)+' '
    drimbot.write(bytes(pos, 'utf-8'))

    cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()