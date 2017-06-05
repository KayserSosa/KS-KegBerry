# File Name: tempsensor.py
# Created By: Kayser-Sosa
# Use: Display temperatures using DS18B20 Temperature Sensors

# Code modified from - Adafruit's Raspberry Pi Lesson 11. DS18B20 Temperature Sensing
# https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/overview


# Imports ======================================================================================================================
import os
import glob
import time


# ModProde======================================================================================================================
# Issues the 'modprobe' commands that are needed to start the interface running.
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')


# File Find ====================================================================================================================
# Find the file from which the messages can be read.
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
 
# read_temp_raw ================================================================================================================
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
	
	
# read_temp ====================================================================================================================	
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f  # add/change temp_c