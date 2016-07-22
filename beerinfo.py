# File Name: KS-kegberry.py
# Created By: Nick Kayser
# Use: Displays information about the beers, how much is left in the kegs, date/time, and kegerator temperatures.

# i only type on this screen


# Imports ======================================================================================================================
import pygame, sys
from pygame.locals import *


# Beer Glass Image Variables ===================================================================================================
pint = pygame.image.load('pint.jpg')
#pint = pygame.transform.scale(pint,(150,150)) # update to correct size
	
mug = pygame.image.load('mug.jpg')
#mug = pygame.transform.scale(mug,(100,100)) # update to correct size
	
pilsner = pygame.image.load('pilsner.jpg')
#pilsner = pygame.transform.scale(pilsner,(100,100)) # update to correct size
	
weizen = pygame.image.load('weizen.jpg')
#weizen = pygame.transform.scale(weizen,(100,100)) # update to correct size
	
tulip = pygame.image.load('tulip.jpg')
#tulip = pygame.transform.scale(tulip,(100,100)) # update to correct size
	
snifter = pygame.image.load('snifter.jpg')
#snifter = pygame.transform.scale(snifter,(100,100)) # update to correct size
	
goblet = pygame.image.load('goblet.jpg')
#goblet = pygame.transform.scale(goblet,(100,100)) # update to correct size

nokeg = pygame.image.load('nokeg.jpg')
#nokeg = pygame.transform.scale(nokeg,(100,100)) # update to correct size

	
# Beer 1 (Left Tap ) Variables =========================================================================================================
beer1name = "N/A" # notes about length here
beer1style = "N/A" # notes about length here
beer1OG = "OG: N/A" # notes about layout here
beer1ibu = "IBU: N/A" # notes about layout here
beer1abv = "ABV: N/A" # notes about layout here
beer1glasspic = nokeg # select from Beer Glass Variables
		

# Beer 2 (Middle Tap) Variables ========================================================================================================
beer2name = "Solitaire Session Ale" # notes about length here
beer2style = "English Pale Ale" # notes about length here
beer2OG = "OG: 1.050 SG" # notes about layout here
beer2ibu = "IBU: 46.6" # notes about layout here
beer2abv = "ABV: 5.1%/VOL" # notes about layout here
beer2glasspic = pint # select from Beer Glass Variables
		

# Beer 3 (Right Tap) Variables =========================================================================================================
beer3name = "Liberty Cream Ale" # notes about length here
beer3style = "American Amber Ale" # notes about length here
beer3OG = "OG: 1.046 SG" # notes about layout here
beer3ibu = "IBU: 16.7" # notes about layout here
beer3abv = "ABV: 4.7%/VOL" # notes about layout here
beer3glasspic = mug # select from Beer Glass Variables
