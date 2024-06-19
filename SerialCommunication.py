import serial 
import time 
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1) 
def write_read(): 
    time.sleep(0.01) 
    data = arduino.readline() 
    return data 
while True: 
	value = write_read() 
	print(value) # printing the value 
