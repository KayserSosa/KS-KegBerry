#!/usr/bin/python

# intro notes here
# created by, etc...


# instead of tweet, email or post value incase of power outage or reboot and a way to add to total
	# or find a way to keep values if power lost, store current values to another file, check file before reloading
# add temp, date, time to bottom
# justify text, left, right, center
#maybe rotating backgrounds? if possible


# Imports ======================================================================================================================
import os
import time
import math
import logging
import pygame, sys
from pygame.locals import *
import RPi.GPIO as GPIO
from flowmeter import *
from beerinfo import *


# GPIO Setup ===================================================================================================================
GPIO.setmode(GPIO.BCM) # use real GPIO numbering
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Left Tap, Beer 1
GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Middle Tap, Beer 2
GPIO.setup(25,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Right Tap, Beer 3
# Flow Meter Wiring: Red = 5-24VDC, Black = Ground, Yellow = GPIO Pin


# Initialize Pygame ============================================================================================================
pygame.init()


# Display Window Setup =========================================================================================================
VIEW_WIDTH = 800 # my numbers 800, original number 1024
VIEW_HEIGHT = 600 # my numbers 600, original number 576
pygame.display.set_caption('KayserSosa Kegberry')


# Hide the Mouse ===============================================================================================================
pygame.mouse.set_visible(False)


# Flow Meters Setup ============================================================================================================
flowMeter1 = FlowMeter('gallon', ["beer"]) # Left Tap, Beer 1
flowMeter2 = FlowMeter('gallon', ["beer"]) # Middle Tap, Beer 2
flowMeter3 = FlowMeter('gallon', ["beer"]) # Right Tap, Beer 3
# Inputs - FlowMeter('displayFormat', ['beverage'])
# displayFormat (select ONE): liter, pint, gallon
# beverage = beer


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
screen = pygame.display.set_mode((VIEW_WIDTH,VIEW_HEIGHT), FULLSCREEN, 32)
windowInfo = pygame.display.Info()

#screen = pygame.display.set_mode((VIEW_WIDTH,VIEW_HEIGHT)) # use for windows testing only
FONTSIZE = 48 # may not be needed
LINEHEIGHT = 28 # may not be needed
screenfont = pygame.font.SysFont(None, FONTSIZE) # may not be needed


# Backgrounds Setup ============================================================================================================
#background = pygame.Surface(screen.get_size())
#background = background.convert()
background = pygame.image.load('Beer-Background.jpg')


# Rendering ====================================================================================================================
def renderThings(flowMeter1, flowMeter2, flowMeter3, screen, screenfont, 
	pint, mug, pilsner, weizen, flute, tulip, snifter, goblet,
	beer1name, beer1style, beer1OG, beer1ibu, beer1abv, beer1glass, beer1glasspic,
	beer2name, beer2style, beer2OG, beer2ibu, beer2abv, beer2glass, beer2glasspic,
	beer3name, beer3style, beer3OG, beer3ibu, beer3abv, beer3glass, beer3glasspic):

	# Clear the screen
	screen.blit(background,(0,0))

	#text edits
	#https://pygame-zero.readthedocs.io/en/latest/ptext.html
	
	# Beer 1 Details - Left Tap ================================================================================================
	
	# Beer 1 Tap
	screenfont = pygame.font.SysFont(None, 60)
	screenfont.set_underline(1)
	rendered = screenfont.render("Left Tap", True, BEER1Text, BEER1Bg)
	screen.blit(rendered, (0, 0))
	
	# Beer 1 Poured
	if flowMeter1.enabled:
		text = screenfont.render(flowMeter1.getFormattedTotalPour(), True, BEER1Text, BEER1Bg)
		textRect = text.get_rect()
		screen.blit(text, (0, 60))
				
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
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer1glass, True, BEER1Text, BEER1Bg)
	screen.blit(rendered, (0, 325))
	screen.blit(beer1glasspic, (0, 360))

	
	# Beer 2 Details - Middle Tap ==============================================================================================
	
	#https://stackoverflow.com/questions/34013119/pygame-text-anchor-right
	# justify center
	
	# Beer 2 Tap
	screenfont = pygame.font.SysFont(None, 60)
	screenfont.set_underline(1)
	rendered = screenfont.render("Middle Tap", True, BEER2Text, BEER2Bg)
	screen.blit(rendered, (266, 0))

	# Beer 2 Poured
	if flowMeter2.enabled:
		text = screenfont.render(flowMeter2.getFormattedTotalPour(), True, BEER2Text, BEER2Bg)
		textRect = text.get_rect()
		screen.blit(text, (266, 60))
				
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
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer2glass, True, BEER2Text, BEER2Bg)
	screen.blit(rendered, (266, 325))
	screen.blit(beer2glasspic, (266, 360))
	
	# Beer 3 Details - Right Tap ===============================================================================================
	
	#https://stackoverflow.com/questions/34013119/pygame-text-anchor-right
	#justify right
	
	# Beer 3 Tap
	screenfont = pygame.font.SysFont(None, 60)
	screenfont.set_underline(1)
	rendered = screenfont.render("Right Tap", True, BEER3Text, BEER3Bg)
	screen.blit(rendered, (532, 0))

	# Beer 3 Poured
	if flowMeter3.enabled:
		text = screenfont.render(flowMeter3.getFormattedTotalPour(), True, BEER3Text, BEER3Bg)
		textRect = text.get_rect()
		screen.blit(text, (532, 60))
				
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
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(beer3glass, True, BEER3Text, BEER3Bg)
	screen.blit(rendered, (532, 325))
	screen.blit(beer2glasspic, (532, 360))

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
	
	# Kegerator Temp ===========================================================================================================
	# right justified temp
	
	# Date / Time ==============================================================================================================
	screenfont = pygame.font.SysFont(None, 35)
	rendered = screenfont.render(time.strftime("%I:%M:%S %p - %Y/%m/%d"), True, WHITE, BLACK)
	screen.blit(rendered, (0, 575))
	# time may be wrong due to internet blocking, unblock and try
	
	# Display everything
	pygame.display.flip()

    
#what is this doing? =======================================================================================================
# is it needed

# Beer, on Pin 23.
def doAClick1(channel):
  currentTime = int(time.time() * FlowMeter.MS_IN_A_SECOND)
  if flowMeter1.enabled == True:
    flowMeter1.update(currentTime)

# Beer, on Pin 24.
def doAClick2(channel):
  currentTime = int(time.time() * FlowMeter.MS_IN_A_SECOND)
  if flowMeter2.enabled == True:
    flowMeter2.update(currentTime)

# Beer, on Pin 25.
def doAClick3(channel):
  currentTime = int(time.time() * FlowMeter.MS_IN_A_SECOND)
  if flowMeter3.enabled == True:
    flowMeter3.update(currentTime)

GPIO.add_event_detect(23, GPIO.RISING, callback=doAClick1, bouncetime=20) # Beer 1, on Pin 23
GPIO.add_event_detect(24, GPIO.RISING, callback=doAClick2, bouncetime=20) # Beer 2, on Pin 24
GPIO.add_event_detect(25, GPIO.RISING, callback=doAClick3, bouncetime=20) # Beer 3, on Pin 24


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
	if (flowMeter1.thisPour <= 0.23 and currentTime - flowMeter1.lastClick > 2000):
		flowMeter1.thisPour = 0.0
    
	if (flowMeter2.thisPour <= 0.23 and currentTime - flowMeter2.lastClick > 2000):
		flowMeter2.thisPour = 0.0
		
	if (flowMeter3.thisPour <= 0.23 and currentTime - flowMeter3.lastClick > 2000):
		flowMeter3.thisPour = 0.0

	# Update the screen
	renderThings(flowMeter1, flowMeter2, flowMeter3, screen, screenfont, 
		pint, mug, pilsner, weizen, flute, tulip, snifter, goblet,
		beer1name, beer1style, beer1OG, beer1ibu, beer1abv, beer1glass, beer1glasspic,
		beer2name, beer2style, beer2OG, beer2ibu, beer2abv, beer2glass, beer2glasspic,
		beer3name, beer3style, beer3OG, beer3ibu, beer3abv, beer3glass, beer3glasspic)
