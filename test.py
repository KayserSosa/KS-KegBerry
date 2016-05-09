import os
import time
import math
import logging
import pygame, sys
from pygame.locals import *
import RPi.GPIO as GPIO

# set up pygame
pygame.init()

# set up the window
VIEW_WIDTH = 1024
VIEW_HEIGHT = 576
pygame.display.set_caption('test') # change caption
view_mode = 'normal'

# hide the mouse
pygame.mouse.set_visible(False)

# set up the colors
BLACK = (0,0,0)
WHITE = (255,255,255)

# set up the window surface
windowSurface = pygame.display.set_mode((VIEW_WIDTH,VIEW_HEIGHT), FULLSCREEN, 32) 
windowInfo = pygame.display.Info()
FONTSIZE = 48
LINEHEIGHT = 28
basicFont = pygame.font.SysFont(None, FONTSIZE)

# set up the backgrounds
bg = pygame.image.load('by-the-glass-mini-infographic.png')
#image=pygame.image.load("by-the-glass-mini-infographic.png").convert_alpha()

def renderThings(windowSurface, basicFont):
  # Clear the screen
  windowSurface.blit(bg,(0,0))

  # Display everything
  pygame.display.flip()



#while True: 
#	for event in pygame.event.get(): 
#		if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE): 
#			windowSurface.fill(WHITE) 
#			windowSurface.blit(bg, (0,0)) 
#			pygame.display.flip()
#pygame.quit()


# main loop
while True:
  # Handle keyboard events
  for event in pygame.event.get():
    if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
      GPIO.cleanup()
      pygame.quit()
      sys.exit()

  # Update the screen
  renderThings(windowSurface, basicFont)
