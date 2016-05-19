#!/usr/bin/python

# intro notes here
# created by, etc...

# i only type on this screen


# Imports ======================================================================================================================
import pygame, sys
from pygame.locals import *


# Beer Glass Image Variables ===================================================================================================
pint = pygame.image.load('pint.jpg')
pint = pygame.transform.scale(pint,(150,150)) # update to correct size
	
mug = pygame.image.load('mug.jpg')
mug = pygame.transform.scale(mug,(100,100)) # update to correct size
	
pilsner = pygame.image.load('pilsner.jpg')
pilsner = pygame.transform.scale(pilsner,(100,100)) # update to correct size
	
weizen = pygame.image.load('weizen.jpg')
weizen = pygame.transform.scale(weizen,(100,100)) # update to correct size
	
tulip = pygame.image.load('tulip.jpg')
tulip = pygame.transform.scale(tulip,(100,100)) # update to correct size
	
snifter = pygame.image.load('snifter.jpg')
snifter = pygame.transform.scale(snifter,(100,100)) # update to correct size
	
goblet = pygame.image.load('goblet.jpg')
goblet = pygame.transform.scale(goblet,(100,100)) # update to correct size

	
# Beer 1 (Left Tap ) Variables =========================================================================================================
beer1name = "Autumn Amber Ale" # notes about length here
beer1style = "American Amber Ale" # notes about length here
beer1OG = "OG: 1.048 SG" # notes about layout here
beer1ibu = "IBU: 13.6" # notes about layout here
beer1abv = "ABV: 4.8%" # notes about layout here
beer1glass = "Pint Glass" # notes about layout here
beer1glasspic = pint # select from Beer Glass Variables
		

# Beer 2 (Middle Tap) Variables ========================================================================================================
beer2name = "Beer2 Name" # notes about length here
beer2style = "Beer2 Style" # notes about length here
beer2OG = "OG: Beer2 SG" # notes about layout here
beer2ibu = "IBU: Beer2" # notes about layout here
beer2abv = "ABV: Beer2%/VOL" # notes about layout here
beer2glass = "Beer2 Glass" # notes about layout here
beer2glasspic = pilsner # select from Beer Glass Variables
		

# Beer 3 (Right Tap) Variables =========================================================================================================
beer3name = "Beer3 Name" # notes about length here
beer3style = "Beer3 Style" # notes about length here
beer3OG = "OG: Beer3 SG" # notes about layout here
beer3ibu = "IBU: Beer3" # notes about layout here
beer3abv = "ABV: Beer3%/VOL" # notes about layout here
beer3glass = "Beer3 Glass" # notes about layout here
beer3glasspic = mug # select from Beer Glass Variables
