#!/usr/bin/env python3
import serial
import thingspeak
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.reset_input_buffer()
    channel_id = 1707389
    key = "B4XFISTMGQ65143C"
    url = 'https://api.thingspeak.com/update'
    ts = thingspeak.Channel(channel_id, key, url)
    data = ""
    while True:
        ser.write(b"100\n")
        ser.write(b"0\n")
        ser.write(b"255\n")
        ser.write(b"255\n")
        ser.write(b"1\n")
        line = ser.readline().decode('utf-8').rstrip()
        data.strip(",")
        print(data)
        time.sleep(1)