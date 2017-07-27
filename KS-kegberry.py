# File Name: KS-kegberry.py
# Created By: Kayser-Sosa, with help from ThatGuyYouKnow and JackBurtonn.
# Use: Displays information about the beers, how much is left in the kegs, date/time, and kegerator temperature.

# Code modified from - Adafruit Kegomatic
# https://learn.adafruit.com/adafruit-keg-bot

# Converts liter to gal and back, didn't want to figure out the flowmeter.py code at this time.
# Store current values to flowMeterValues.txt, checks file before reloading.


# Imports ======================================================================================================================
import os
import time
import math
import logging
import pygame, sys
from pygame.locals import *
import RPi.GPIO as GPIO
from flowmeter import *
from tempsensor import *
from beerinfo import *


# GPIO Setup ===================================================================================================================
GPIO.setmode(GPIO.BCM) # use real GPIO numbering
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Left Tap, Beer 1
GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Middle Tap, Beer 2
GPIO.setup(25,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Right Tap, Beer 3
# Flow Meter Wiring: Red = 5-24VDC, Black = Ground, Yellow = GPIO Pin


# Initialize Pygame ============================================================================================================
pygame.init()


# Read/Write File ==============================================================================================================
FILENAME = 'flowMeterValues.txt'


# Hide the Mouse ===============================================================================================================
pygame.mouse.set_visible(False)


# Flow Meters Setup ============================================================================================================
flowMeter1 = FlowMeter('gallon') # Left Tap, Beer 1
flowMeter2 = FlowMeter('gallon') # Middle Tap, Beer 2
flowMeter3 = FlowMeter('gallon') # Right Tap, Beer 3
# Inputs - FlowMeter('displayFormat')
					# displayFormat (select ONE): liter, pint, gallon
				

# Read Saved Values from flowMeterValues.txt ++=================================================================================
# The text file is in gallons and totalPour is in liters so each needs to be converted from gal to L
with open(FILENAME,'r') as f:
	lines = f.readlines()
	flowMeter1.totalPour = float(lines[0]) * 3.7854
	flowMeter2.totalPour = float(lines[1]) * 3.7854
	flowMeter3.totalPour = float(lines[2]) * 3.7854
f.closed


# Colors Setup =================================================================================================================
# http://www.rapidtables.com/web/color/RGB_Color.htm
BLACK = (0,0,0)
WHITE = (255,255,255)
TGREEN = (80,200,100) # PC Terminal Green
RED = (255,0,0)
ORANGE = (255,128,0)


# Text Backgroud Color for each beer
BEER1Bg = None
BEER2Bg = None
BEER3Bg = None


# Window Surface Setup =========================================================================================================
VIEW_WIDTH = 800 # my numbers 800, original number 1024
VIEW_HEIGHT = 600 # my numbers 600, original number 576
pygame.display.set_caption('KayserSosa Kegberry')
screen = pygame.display.set_mode((VIEW_WIDTH,VIEW_HEIGHT), FULLSCREEN, 32)
windowInfo = pygame.display.Info()


# Backgrounds Setup ============================================================================================================
background = pygame.image.load('Beer-Background.jpg')


# Rendering ====================================================================================================================
# Text Formating - https://pygame-zero.readthedocs.io/en/latest/ptext.html
def renderThings(flowMeter1, flowMeter2, flowMeter3, screen, 
	pint, mug, pilsner, weizen, tulip, snifter, goblet, teku, stange,
	beer1name, beer1srm, beer1style, beer1OG, beer1ibu, beer1abv, beer1glasspic, beer1textcolor,
	beer2name, beer2srm, beer2style, beer2OG, beer2ibu, beer2abv, beer2glasspic, beer2textcolor,
	beer3name, beer3srm, beer3style, beer3OG, beer3ibu, beer3abv, beer3glasspic, beer3textcolor):

	# Clear the screen
	screen.blit(background,(0,0))

	
	# Beer 1 Details - Left Tap ================================================================================================
	# Left Justified
	
	# Beer 1 Tap
	screenfont = pygame.font.SysFont(None, 60)
	rendered = screenfont.render("Left Tap", True, beer1textcolor, BEER1Bg)
	screen.blit(rendered, (0, 0))
		
	# Beer 1 Poured
	screenfont.set_underline(1)
	if flowMeter1.enabled:
		rendered = screenfont.render(flowMeter1.getFormattedTotalPour() + " / 5.0 gal", True, beer1textcolor, BEER1Bg)
		screen.blit(rendered, (0, 60))
	screenfont.set_underline(0)
				
	# Beer 1 Name
	screenfont = pygame.font.SysFont(None, 40)
	rendered = screenfont.render(beer1name, True, beer1textcolor, BEER1Bg)
	screen.blit(rendered, (0, 120))
		
	# Beer 1 SRM (Color) Line Separator
	pygame.draw.rect(screen, beer1srm, [0,158,256,20])
	#screenfont = pygame.font.SysFont(None, 20)
	#rendered = screenfont.render('================================', True, beer1textcolor, BEER1Bg)
	#screen.blit(rendered, (0, 160))
			
	# Beer 1 Style
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer1style, True, beer1textcolor, BEER1Bg)
	screen.blit(rendered, (0, 185))
	
	# Beer 1 Original Gravity (OG)
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer1OG, True, beer1textcolor, BEER1Bg)
	screen.blit(rendered, (0, 220))
	
	# Beer 1 International Bittering Units (IBU)
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer1ibu, True, beer1textcolor, BEER1Bg)
	screen.blit(rendered, (0, 255))
	
	# Beer 1 Alcohol / Volume (ABV)
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer1abv, True, beer1textcolor, BEER1Bg)
	screen.blit(rendered, (0, 290))
	
	# Beer 1 Glass
	screen.blit(beer1glasspic, (0, 325))

	
	# Beer 2 Details - Middle Tap ==============================================================================================
	# Center Justified
	
	# Beer 2 Tap
	screenfont = pygame.font.SysFont(None, 60)
	rendered = screenfont.render("Middle Tap", True, beer2textcolor, BEER2Bg)
	screen.blit(rendered, (((VIEW_WIDTH / 2) - (rendered.get_rect().width / 2)), 0))
	
	# Beer 2 Poured
	screenfont.set_underline(1)
	if flowMeter2.enabled:
		rendered = screenfont.render(flowMeter2.getFormattedTotalPour() + " / 5.0 gal", True, beer2textcolor, BEER2Bg)
		screen.blit(rendered, (((VIEW_WIDTH / 2) - (rendered.get_rect().width / 2)), 60))
	screenfont.set_underline(0)
				
	# Beer 2 Name
	screenfont = pygame.font.SysFont(None, 40)
	rendered = screenfont.render(beer2name, True, beer2textcolor, BEER2Bg)
	screen.blit(rendered, (((VIEW_WIDTH / 2) - (rendered.get_rect().width / 2)), 120))
		
	# Beer 2 SRM (Color) Line Separator
	pygame.draw.rect(screen, beer2srm, [272,158,256,20])
	#screenfont = pygame.font.SysFont(None, 20)
	#rendered = screenfont.render('================================', True, beer2textcolor, BEER2Bg)
	#screen.blit(rendered, (((VIEW_WIDTH / 2) - (rendered.get_rect().width / 2)), 160))
							
	# Beer 2 Style
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer2style, True, beer2textcolor, BEER2Bg)
	screen.blit(rendered, (((VIEW_WIDTH / 2) - (rendered.get_rect().width / 2)), 185))
	
	# Beer 2 Original Gravity (OG)
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer2OG, True, beer2textcolor, BEER2Bg)
	screen.blit(rendered, (((VIEW_WIDTH / 2) - (rendered.get_rect().width / 2)), 220))
	
	# Beer 2 International Bittering Units (IBU)
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer2ibu, True, beer2textcolor, BEER2Bg)
	screen.blit(rendered, (((VIEW_WIDTH / 2) - (rendered.get_rect().width / 2)), 255))
	
	# Beer 2 Alcohol / Volume (ABV)
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer2abv, True, beer2textcolor, BEER2Bg)
	screen.blit(rendered, (((VIEW_WIDTH / 2) - (rendered.get_rect().width / 2)), 290))
	
	# Beer 2 Glass
	screen.blit(beer2glasspic, (((VIEW_WIDTH / 2) - (rendered.get_rect().width / 2)), 325))
	
	# Beer 3 Details - Right Tap ===============================================================================================
	# Right Justified
	
	# Beer 3 Tap
	screenfont = pygame.font.SysFont(None, 60)
	rendered = screenfont.render("Right Tap", True, beer3textcolor, BEER3Bg)
	screen.blit(rendered, ((VIEW_WIDTH - rendered.get_rect().width), 0))
	
	# Beer 3 Poured
	screenfont.set_underline(1)
	if flowMeter3.enabled:
		rendered = screenfont.render(flowMeter3.getFormattedTotalPour() + " / 5.0 gal", True, beer3textcolor, BEER3Bg)
		screen.blit(rendered, ((VIEW_WIDTH - rendered.get_rect().width), 60))
	screenfont.set_underline(0)
				
	# Beer 3 Name
	screenfont = pygame.font.SysFont(None, 40)
	rendered = screenfont.render(beer3name, True, beer3textcolor, BEER3Bg)
	screen.blit(rendered, ((VIEW_WIDTH - rendered.get_rect().width), 120))
		
	# Beer 3 SRM (Color) Line Separator
	pygame.draw.rect(screen, beer3srm, [(VIEW_WIDTH - rendered.get_rect().width),158,256,20])
	#screenfont = pygame.font.SysFont(None, 20)
	#rendered = screenfont.render('================================', True, beer3textcolor, BEER3Bg)
	#screen.blit(rendered, ((VIEW_WIDTH - rendered.get_rect().width), 160))
		
	# Beer 3 Style
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer3style, True, beer3textcolor, BEER3Bg)
	screen.blit(rendered, ((VIEW_WIDTH - rendered.get_rect().width), 185))
	
	# Beer 3 Original Gravity (OG)
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer3OG, True, beer3textcolor, BEER3Bg)
	screen.blit(rendered, ((VIEW_WIDTH - rendered.get_rect().width), 220))
	
	# Beer 3 International Bittering Units (IBU)
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer3ibu, True, beer3textcolor, BEER3Bg)
	screen.blit(rendered, ((VIEW_WIDTH - rendered.get_rect().width), 255))
	
	# Beer 3 Alcohol / Volume (ABV)
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer3abv, True, beer3textcolor, BEER3Bg)
	screen.blit(rendered, ((VIEW_WIDTH - rendered.get_rect().width), 290))
	
	# Beer 3 Glass
	screen.blit(beer3glasspic, ((VIEW_WIDTH - rendered.get_rect().width), 325))

	
	# Kegerator Temps ===========================================================================================================
	# Using Pin 4
	# Left Justified	
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render("Kegerator Temp: " + str(round(read_temp(),1)) + " F", True, WHITE, BLACK)
	screen.blit(rendered, ((VIEW_WIDTH - rendered.get_rect().width), 575))
			
	
	# Date / Time ==============================================================================================================
	# Date & Time required internet access to initially set & on reboots
	# Right Justified
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(time.strftime("%I:%M:%S %p - %Y/%m/%d"), True, WHITE, BLACK)
	screen.blit(rendered, (0, 575))
	
		
	# Display everything
	pygame.display.flip()

    
# Flowmeter Updates ============================================================================================================
# Beer 1, on Pin 23.
def doAClick1(channel):
	currentTime = int(time.time() * FlowMeter.MS_IN_A_SECOND)
	if flowMeter1.enabled == True:
		flowMeter1.update(currentTime)
		saveValues(flowMeter1, flowMeter2, flowMeter3)

# Beer 2, on Pin 24.
def doAClick2(channel):
	currentTime = int(time.time() * FlowMeter.MS_IN_A_SECOND)
	if flowMeter2.enabled == True:
		flowMeter2.update(currentTime)
		saveValues(flowMeter1, flowMeter2, flowMeter3)

# Beer 3, on Pin 25.
def doAClick3(channel):
	currentTime = int(time.time() * FlowMeter.MS_IN_A_SECOND)
	if flowMeter3.enabled == True:
		flowMeter3.update(currentTime)
		saveValues(flowMeter1, flowMeter2, flowMeter3)

GPIO.add_event_detect(23, GPIO.RISING, callback=doAClick1, bouncetime=20) # Beer 1, on Pin 23
GPIO.add_event_detect(24, GPIO.RISING, callback=doAClick2, bouncetime=20) # Beer 2, on Pin 24
GPIO.add_event_detect(25, GPIO.RISING, callback=doAClick3, bouncetime=20) # Beer 3, on Pin 24


# Erase & Save New Data to File +===============================================================================================
def saveValues(flowMeter1, flowMeter2, flowMeter3):
	f = open(FILENAME, 'w')
	if flowMeter1.enabled == True:
		f.write(flowMeter1.getFormattedTotalPour() + "\n")
	if flowMeter2.enabled == True:
		f.write(flowMeter2.getFormattedTotalPour() + "\n")
	if flowMeter3.enabled == True:
		f.write(flowMeter3.getFormattedTotalPour() + "\n")
	f.close()


# Main Never Ending Loop =======================================================================================================
while True:
	# Handle keyboard events
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
			GPIO.cleanup()
			pygame.quit()
			sys.exit()
		elif event.type == KEYUP and event.key == K_1:
			flowMeter1.enabled = not(flowMeter1.enabled)
		elif event.type == KEYUP and event.key == K_2:
			flowMeter2.enabled = not(flowMeter2.enabled)
		elif event.type == KEYUP and event.key == K_3:
			flowMeter3.enabled = not(flowMeter3.enabled)
		elif event.type == KEYUP and event.key == K_8:
			flowMeter1.clear()
		elif event.type == KEYUP and event.key == K_9:
			flowMeter2.clear()
		elif event.type == KEYUP and event.key == K_0:
			flowMeter3.clear()
  	currentTime = int(time.time() * FlowMeter.MS_IN_A_SECOND)

	# Update the screen
	renderThings(flowMeter1, flowMeter2, flowMeter3, screen, 
		pint, mug, pilsner, weizen, tulip, snifter, goblet, teku, stange,
		beer1name, beer1srm, beer1style, beer1OG, beer1ibu, beer1abv, beer1glasspic, beer1textcolor,
		beer2name, beer2srm, beer2style, beer2OG, beer2ibu, beer2abv, beer2glasspic, beer2textcolor,
		beer3name, beer3srm, beer3style, beer3OG, beer3ibu, beer3abv, beer3glasspic, beer3textcolor)