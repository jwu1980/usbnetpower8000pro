#!/usr/bin/python

# It is a command-line tool for simply ON/OFF "USB Net Power 8800 pro" over
# serail port (USB CDC) on Linux. Make sure that your device shows up as
#  - lsusb:
#   ID 04d8:000a Microchip Technology, Inc. CDC RS-232 Emulation Demo
#  - device: 
#   /dev/ttyACM0
#
# Also, you must install required python modules such as serial and usb before
# lauching this command.
#
# This command requires super user permission.
# Don't forget to change mode as executable.

import serial
import time
import sys
import usb.core

usage = ("Usage: %s on|off|reboot\n")

try:
    cmd = sys.argv[1].lower()
except IndexError:
    cmd = ""

try:
    dev = usb.core.find(idVendor=0x04d8, idProduct=0x000a)
    if dev is None:
        raise ValueError("Device not found")
 
    port = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=3.0)
    if port is None:
        raise ValueError("Fail to connect")
except ValueError:
    sys.exit(-1)

if cmd == "on":
    time.sleep(1)
    port.write("p1=1\r\n")
elif cmd == "off":
    time.sleep(1)
    port.write("p1=0\r\n")
elif cmd == "reboot":
    time.sleep(1)
    port.write("p1=0\r\n")
    time.sleep(1)
    port.write("p1=1\r\n")
else:
    sys.stdout.write(usage % sys.argv[0])

