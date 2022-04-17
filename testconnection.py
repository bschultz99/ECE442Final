#!/usr/bin/env python3
import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.reset_input_buffer()

    while True:
        ser.write(b"100,0,255,255,1\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)