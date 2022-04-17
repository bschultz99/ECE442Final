#!/usr/bin/env python3
import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.reset_input_buffer()

    while True:
        ser.write(b"100\n")
        ser.write(b"0\n")
        ser.write(b"255\n")
        ser.write(b"255\n")
        ser.write(b"1\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)