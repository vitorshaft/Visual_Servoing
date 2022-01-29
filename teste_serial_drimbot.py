import serial
drimbot = serial.Serial(port='COM7', baudrate=9600, timeout=.1)

for i in range(5) :
    comando = input('angulo da base: ')

    