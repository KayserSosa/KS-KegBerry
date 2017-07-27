# File Name: beerinfo.py
# Created By: Kayser-Sosa
# Use: Holds the variables for the beers.
# Only edit these variables, copy to Raspberry Pi, rerun KS-kegberry.py


# Imports ======================================================================================================================
import pygame, sys
from pygame.locals import *


# Beer Glass Image Variables ===================================================================================================
pint = pygame.image.load('pint.jpg')
pint = pygame.transform.scale(pint,(125,225))

weizen = pygame.image.load('weizen.jpg')
weizen = pygame.transform.scale(weizen,(125,225))

goblet = pygame.image.load('goblet.jpg')
goblet = pygame.transform.scale(goblet,(125,225))
	
tulip = pygame.image.load('tulip.jpg')
tulip = pygame.transform.scale(tulip,(125,225))

snifter = pygame.image.load('snifter.jpg')
snifter = pygame.transform.scale(snifter,(125,225))
	
mug = pygame.image.load('mug.jpg')
mug = pygame.transform.scale(mug,(125,225))
	
teku = pygame.image.load('teku.jpg')
teku = pygame.transform.scale(teku,(125,225))

stange = pygame.image.load('stange.jpg')
stange = pygame.transform.scale(stange,(125,225))

pilsner = pygame.image.load('pilsner.jpg')
pilsner = pygame.transform.scale(pilsner,(125,225))

nokeg = pygame.image.load('nokeg.jpg')
nokeg = pygame.transform.scale(nokeg,(125,225))


# Colors SRM & Text Value =======================================================================================================
# http://www.rapidtables.com/web/color/RGB_Color.htm
# SRM HEX Values - http://www.homebrewtalk.com/showthread.php?t=78018

BLACK = (0,0,0)
WHITE = (255,255,255)

RED = (255,0,0) # Used for no keg

TGREEN = (80,200,100) # PC Terminal Green, Slurm

SRM1 = (255,230,153) #FFE699
SRM2 = (255,216,120) #FFD878
SRM3 = (255,202,90) #FFCA5A
SRM4 = (255,191,66) #FFBF42
SRM5 = (251,177,35) #FBB123
SRM6 = (248,166,0) #F8A600
SRM7 = (243,156,0) #F39C00
SRM8 = (235,143,0) #EA8F00
SRM9 = (229,133,0) #E58500
SRM10 = (222,124,0) #DE7C00
SRM11 = (215,114,0) #D77200
SRM12 = (207,105,0) #CF6900
SRM13 = (203,98,0) #CB6200
SRM14 = (195,89,0) #C35900
SRM15 = (187,81,0) #BB5100
SRM16 = (181,76,0) #B54C00 
SRM17 = (176,69,0) #B04500
SRM18 = (166,62,0) #A63E00
SRM19 = (161,55,0) #A13700
SRM20 = (155,50,0) #9B3200
SRM21 = (149,45,0) #952D00
SRM22 = (142,41,0) #8E2900
SRM23 = (136,35,0) #882300
SRM24 = (130,30,0) #821E00
SRM25 = (123,26,0) #7B1A00
SRM26 = (119,25,0) #771900
SRM27 = (112,20,0) #701400
SRM28 = (106,14,0) #6A0E00
SRM29 = (102,13,0) #660D00
SRM30 = (94,11,0) #5E0B00
SRM31 = (90,10,2) #5A0A02
SRM32 = (96,9,3) #600903
SRM33 = (82,9,7) #520907
SRM34 = (76,5,5) #4C0505
SRM35 = (71,6,6) #470606
SRM36 = (68,6,7) #440607
SRM37 = (63,7,8) #3F0708
SRM38 = (59,6,7) #3B0607
SRM39 = (58,7,11) #3A070B
SRM40 = (54,8,10) #36080A

# ABV Calculator
# https://www.brewersfriend.com/abv-calculator/

# IBU Calculator
# https://www.brewersfriend.com/ibu-calculator/

# SRM Calculator
# https://www.brewersfriend.com/srm-calculator/
# http://www.franklinbrew.org/wp/wp-content/uploads/2011/01/srm.jpg

	
# Beer 1 (Left Tap ) Variables =========================================================================================================
beer1name = "No Keg" # 20 char limit
beer1srm = RED # srm color value
beer1style = "Style" # 19 char limit
beer1OG = "OG: 0 SG" # layout like OG: #.### SG
beer1ibu = "IBU: 0" # layout like IBU: ##.#
beer1abv = "ABV: 0%/VOL" # layout like ABV: #.#%/VOL
beer1glasspic = nokeg # select from Beer Glass Variables
beer1textcolor = RED # text color of beer info
		

# Beer 2 (Middle Tap) Variables ========================================================================================================
beer2name = "Cider" # 20 char limit
beer2srm = SRM2 # srm color value
beer2style = "Common Cider" # 19 char limit
beer2OG = "OG: 1.048 SG" # layout like OG: #.### SG
beer2ibu = "IBU: 0.0" # layout like IBU: ##.#
beer2abv = "ABV: 6.04%/VOL" # layout like ABV: #.#%/VOL
beer2glasspic = teku # select from Beer Glass Variables
beer2textcolor = BLACK # text color of beer info
		

# Beer 3 (Right Tap) Variables =========================================================================================================
beer3name = "Hex Nut Brown Ale" # 20 char limit
beer3srm = SRM23 # srm color value
beer3style = "American Brown Ale" # 19 char limit
beer3OG = "OG: 1.046 SG" # layout like OG: #.### SG
beer3ibu = "IBU: 33.1" # layout like IBU: ##.#
beer3abv = "ABV: 4.73%/VOL" # layout like ABV: #.#%/VOL
beer3glasspic = pint # select from Beer Glass Variables
beer3textcolor = BLACK # text color of beer info