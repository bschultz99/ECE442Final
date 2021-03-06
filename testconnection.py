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
    fans = 100
    red = 0
    green = 255
    blue = 255
    servo = 0
    while True:
        ser.write(b"100\n")
        ser.write(b"0\n")
        ser.write(b"255\n")
        ser.write(b"255\n")
        ser.write(b"0\n")
        line = ser.readline().decode('utf-8').rstrip()
        thingspeak_field1 = {"field1": fans}
        thingspeak_field2 = {"field2": red}
        thingspeak_field3 = {"field3": green}
        thingspeak_field4 = {"field4": blue}
        thingspeak_field6 = {"field6": servo}
        if (len(line.split(",")) == 3):
            thingspeak_field5 = {"field5": line.split(",")[2]}
            thingspeak_field7 = {"field7": line.split(",")[0]}
            thingspeak_field8 = {"field8": line.split(",")[1]}
            ts.update(thingspeak_field5)
            ts.update(thingspeak_field7)
            ts.update(thingspeak_field8)
        ts.update(thingspeak_field1)
        ts.update(thingspeak_field2)
        ts.update(thingspeak_field3)
        ts.update(thingspeak_field4)
        ts.update(thingspeak_field6)
        time.sleep(1)