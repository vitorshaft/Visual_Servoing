from cv2 import *
import matplotlib.pyplot as plt

# initialize the camera
# If you have multiple camera connected with
# current device, assign a value in cam_port
# variable according to that
cam_port = 1
cam = VideoCapture(cam_port)

# reading the input using the camera
result, image = cam.read()

# If image will detected without any error,
# show result
if result:
    while True:
        _, frame = cam.read()

        # showing result, it take frame name and image
        # output
        imshow("objeto_alvo", frame)

        # If keyboard interrupt occurs, destroy image
        # window
        key = waitKey(1)

        if key == 27:

            imwrite("objeto_alvo.png", frame)
            break
    destroyWindow("objeto_alvo")

# If captured image is corrupted, moving to else part
else:
    print("No image detected. Please! try again")

img = imread("objeto_alvo.png",0)
histg = calcHist([img],[0],None,[256],[0,256])

plt.plot(histg)
plt.show()