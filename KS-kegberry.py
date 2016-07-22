# File Name: KS-kegberry.py
# Created By: Nick Kayser
# With Help From: Andrew Fleer and P.J. Lorenz
# Use: Displays information about the beers, how much is left in the kegs, date/time, and kegerator temperatures.

# Code modified from - Adafruit Kegomatic
# https://learn.adafruit.com/adafruit-keg-bot


# convert liter to gal and back because didnt want to fig out flowmeter.py
# store current values to another file, check file before reloading

# TO DO YET, MAYBE
# add temp to bottom left
# justify text, left, right, center
# resize text fonts according to space provided
# maybe rotating backgrounds? if possible
# remove all unwanted/unneeded items


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
flowMeter1 = FlowMeter('gallon', ["beer"]) # Left Tap, Beer 1
flowMeter2 = FlowMeter('gallon', ["beer"]) # Middle Tap, Beer 2
flowMeter3 = FlowMeter('gallon', ["beer"]) # Right Tap, Beer 3
# Inputs - FlowMeter('displayFormat', ['beverage'])
					# displayFormat (select ONE): liter, pint, gallon
					# beverage = beer


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

# Text Color for each beer
BEER1Text = ORANGE
BEER2Text = RED
BEER3Text = WHITE

# Text Backgroud Color for each beer
BEER1Bg = BLACK
BEER2Bg = BLACK
BEER3Bg = BLACK


# Window Surface Setup =========================================================================================================
VIEW_WIDTH = 800 # my numbers 800, original number 1024
VIEW_HEIGHT = 600 # my numbers 600, original number 576
pygame.display.set_caption('KayserSosa Kegberry')
screen = pygame.display.set_mode((VIEW_WIDTH,VIEW_HEIGHT), FULLSCREEN, 32)
windowInfo = pygame.display.Info()


# Backgrounds Setup ============================================================================================================
background = pygame.image.load('Beer-Background.jpg')


# Rendering ====================================================================================================================
def renderThings(flowMeter1, flowMeter2, flowMeter3, screen, 
	pint, mug, pilsner, weizen, tulip, snifter, goblet,
	beer1name, beer1style, beer1OG, beer1ibu, beer1abv, beer1glasspic,
	beer2name, beer2style, beer2OG, beer2ibu, beer2abv, beer2glasspic,
	beer3name, beer3style, beer3OG, beer3ibu, beer3abv, beer3glasspic):

	# Clear the screen
	screen.blit(background,(0,0))

	#text formatting
	#https://pygame-zero.readthedocs.io/en/latest/ptext.html
	
	# Beer 1 Details - Left Tap ================================================================================================
	
	# Beer 1 Tap
	screenfont = pygame.font.SysFont(None, 60)
	screenfont.set_underline(1)
	rendered = screenfont.render("Left Tap", True, BEER1Text, BEER1Bg)
	screen.blit(rendered, (0, 0))
	
	# Beer 1 Poured
	if flowMeter1.enabled:
		rendered = screenfont.render(flowMeter1.getFormattedTotalPour() + " / 5.0 gal", True, BEER1Text, BEER1Bg)
		textRect = rendered.get_rect()
		screen.blit(rendered, (0, 60))
				
	# Beer 1 Name
	screenfont = pygame.font.SysFont(None, 40)
	rendered = screenfont.render(beer1name, True, BEER1Text, BEER1Bg)
	screen.blit(rendered, (0, 120))
		
	# Beer 1 Separator Line
	screenfont = pygame.font.SysFont(None, 20)
	rendered = screenfont.render('================================', True, BEER1Text, BEER1Bg)
	screen.blit(rendered, (0, 160))
		
	# Beer 1 Style
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer1style, True, BEER1Text, BEER1Bg)
	screen.blit(rendered, (0, 185))
	
	# Beer 1 Original Gravity (OG)
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer1OG, True, BEER1Text, BEER1Bg)
	screen.blit(rendered, (0, 220))
	
	# Beer 1 International Bittering Units (IBU)
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer1ibu, True, BEER1Text, BEER1Bg)
	screen.blit(rendered, (0, 255))
	
	# Beer 1 Alcohol / Volume (ABV)
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer1abv, True, BEER1Text, BEER1Bg)
	screen.blit(rendered, (0, 290))
	
	# Beer 1 Glass
	screen.blit(beer1glasspic, (0, 325))

	
	# Beer 2 Details - Middle Tap ==============================================================================================
	
	#https://stackoverflow.com/questions/32673965/pygame-blitting-center
	#centering text
	
	
	# Beer 2 Tap
	screenfont = pygame.font.SysFont(None, 60)
	screenfont.set_underline(1)
	rendered = screenfont.render("Middle Tap", True, BEER2Text, BEER2Bg)
	screen.blit(rendered, (266, 0))

	# Beer 2 Poured
	if flowMeter2.enabled:
		rendered = screenfont.render(flowMeter2.getFormattedTotalPour() + " / 5.0 gal", True, BEER2Text, BEER2Bg)
		textRect = rendered.get_rect()
		screen.blit(rendered, (266, 60))
				
	# Beer 2 Name
	screenfont = pygame.font.SysFont(None, 40)
	rendered = screenfont.render(beer2name, True, BEER2Text, BEER2Bg)
	screen.blit(rendered, (266, 120))
		
	# Beer 2 Separator Line
	screenfont = pygame.font.SysFont(None, 20)
	rendered = screenfont.render('================================', True, BEER2Text, BEER2Bg)
	screen.blit(rendered, (266, 160))
		
	# Beer 2 Style
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer2style, True, BEER2Text, BEER2Bg)
	screen.blit(rendered, (266, 185))
	
	# Beer 2 Original Gravity (OG)
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer2OG, True, BEER2Text, BEER2Bg)
	screen.blit(rendered, (266, 220))
	
	# Beer 2 International Bittering Units (IBU)
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer2ibu, True, BEER2Text, BEER2Bg)
	screen.blit(rendered, (266, 255))
	
	# Beer 2 Alcohol / Volume (ABV)
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer2abv, True, BEER2Text, BEER2Bg)
	screen.blit(rendered, (266, 290))
	
	# Beer 2 Glass
	screen.blit(beer2glasspic, (266, 325))
	
	# Beer 3 Details - Right Tap ===============================================================================================
	
	# Beer 3 Tap
	screenfont = pygame.font.SysFont(None, 60)
	screenfont.set_underline(1)
	rendered = screenfont.render("Right Tap", True, BEER3Text, BEER3Bg)
	screen.blit(rendered, (532, 0))  # remove when right justified
	#textRect = rendered.get_rect()
	#textRect.right = 800
	#screen.blit(rendered, textRect)
	
	#https://stackoverflow.com/questions/34013119/pygame-text-anchor-right
	#justify right
	# how to move right aligned items down on screen
	
	# Beer 3 Poured
	if flowMeter3.enabled:
		rendered = screenfont.render(flowMeter3.getFormattedTotalPour() + " / 5.0 gal", True, BEER3Text, BEER3Bg)
		textRect = rendered.get_rect()
		screen.blit(rendered, (532, 60))
				
	# Beer 3 Name
	screenfont = pygame.font.SysFont(None, 40)
	rendered = screenfont.render(beer3name, True, BEER3Text, BEER3Bg)
	screen.blit(rendered, (532, 120))
		
	# Beer 3 Separator Line
	screenfont = pygame.font.SysFont(None, 20)
	rendered = screenfont.render('================================', True, BEER3Text, BEER3Bg)
	screen.blit(rendered, (532, 160))
		
	# Beer 3 Style
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer3style, True, BEER3Text, BEER3Bg)
	screen.blit(rendered, (532, 185))
	
	# Beer 3 Original Gravity (OG)
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer3OG, True, BEER3Text, BEER3Bg)
	screen.blit(rendered, (532, 220))
	
	# Beer 3 International Bittering Units (IBU)
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer3ibu, True, BEER3Text, BEER3Bg)
	screen.blit(rendered, (532, 255))
	
	# Beer 3 Alcohol / Volume (ABV)
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer3abv, True, BEER3Text, BEER3Bg)
	screen.blit(rendered, (532, 290))
	
	# Beer 3 Glass
	screen.blit(beer3glasspic, (532, 325))

	#https://stackoverflow.com/questions/34013119/pygame-text-anchor-right
	#justiry right testing
	
		
	#screenfont = pygame.font.SysFont(None, 35)
	#text = screenfont.render("right justified test", True, BEER3Text, BEER3Bg)
	#textpos = text.get_rect()
	#textpos.centerx = background.get_rect().centerx
	#screen.blit(text, textpos)
	
	#newrendered = rendered.get_rect(right=(532, 600)
	#newrendered.right = 500
	#screen.blit(rendered, newrendered)
	
	# Kegerator Temps ===========================================================================================================
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render("Kegerator Temp: " + str(round(read_temp(),1)) + " F", True, WHITE, BLACK)
	screen.blit(rendered, (532, 575))
			
	
	# Date / Time ==============================================================================================================
	# Date & Time required internet access to initially set
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
  
	# is this needed? ====================================================================
	# Reset flowmeters after each pour (2 secs of inactivity)
#	if (flowMeter1.thisPour <= 0.23 and currentTime - flowMeter1.lastClick > 2000):
#		flowMeter1.thisPour = 0.0
    
#	if (flowMeter2.thisPour <= 0.23 and currentTime - flowMeter2.lastClick > 2000):
#		flowMeter2.thisPour = 0.0
		
#	if (flowMeter3.thisPour <= 0.23 and currentTime - flowMeter3.lastClick > 2000):
#		flowMeter3.thisPour = 0.0

	# Update the screen
	renderThings(flowMeter1, flowMeter2, flowMeter3, screen, 
		pint, mug, pilsner, weizen, tulip, snifter, goblet,
		beer1name, beer1style, beer1OG, beer1ibu, beer1abv, beer1glasspic,
		beer2name, beer2style, beer2OG, beer2ibu, beer2abv, beer2glasspic,
		beer3name, beer3style, beer3OG, beer3ibu, beer3abv, beer3glasspic)