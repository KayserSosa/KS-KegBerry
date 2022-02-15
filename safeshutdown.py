#!/usr/bin/env python3

# https://github.com/TonyLHansen/raspberry-pi-safe-off-switch/

from gpiozero import Button
import os
Button(21).wait_for_press()
os.system("sudo poweroff")