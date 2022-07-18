'''
Script para controle de Servomotores a partir do modulo i2c PCA9685
Layout:

2-4-6-8-10-12-14-16-18-20-22-24-26-28-30-32-34-36-38-40
1-3-5-7- 9-11-13-15-17-19-21-23-25-27-29-31-33-35-37-39 [USB]
[DISPLAY]	[CPU]										[USB]
[POWER]		[HDMI][CAM][AUDIO]							[Ethernet]

Conexoes:
VCC - Pino 1
SDA - Pino 3
SCL - Pino 5
GND - Pino 9

Instalar libs:
sudo pip3 install adafruit-circuitpython-servokit
'''

import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
for i in range(15):
	#descomente linha abaixo para redefinir o intervalo de atuacao de cada servo
	#kit.servo[i].actuation_range = 160
	kit.servo[i].angle = 0
	print("Servo ",i," em 120 graus")
time.sleep(1)
for a in range(15):
	kit.servo[a].angle = 90
	print("Servo ",a," em 30 graus")
time.sleep(1)
