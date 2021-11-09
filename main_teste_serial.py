import serial
import time


porta_serial = serial.Serial('COM6', 57600)
time_delay = 0.01


for i in range(5*40):
    #porta_serial.write(b"B")
    porta_serial.write(b"C")
    time.sleep(time_delay)
    
porta_serial.close()