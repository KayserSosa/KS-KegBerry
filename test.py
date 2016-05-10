# intro notes here


# ==============================================================================================================================
import pygame, sys
from pygame.locals import *


# Initialize Pygame ============================================================================================================
pygame.init()


# Display Window Setup =========================================================================================================
VIEW_WIDTH = 1024
VIEW_HEIGHT = 576
pygame.display.set_caption('KayserSosa Kegberry')
#screen = pygame.display.set_mode((VIEW_WIDTH,VIEW_HEIGHT), FULLSCREEN, 32)   use fullscreen for pi?
screen = pygame.display.set_mode((VIEW_WIDTH,VIEW_HEIGHT)) 


# Colors Setup =================================================================================================================
BLACK = (0,0,0)
WHITE = (255,255,255)


# Rendering ====================================================================================================================
def renderThings(screen):
	# screen.blit(bg,(0,0)) # Clear the screen, needed for images?
	screen.fill(BLACK) # only needed for testing?
	
	
	# Beer Glass Variables =====================================================================================================
	pint = pygame.image.load('pint-glass.jpg') # update image
	pint = pygame.transform.scale(pint,(100,100)) # update to correct size
	
	mug = pygame.image.load('by-the-glass-mini-infographic.png') # update image
	mug = pygame.transform.scale(mug,(100,100)) # update to correct size
	
	pilsner = pygame.image.load('by-the-glass-mini-infographic.png') # update image
	pilsner = pygame.transform.scale(pilsner,(100,100)) # update to correct size
	
	weizen = pygame.image.load('by-the-glass-mini-infographic.png') # update image
	weizen = pygame.transform.scale(weizen,(100,100)) # update to correct size
	
	flute = pygame.image.load('by-the-glass-mini-infographic.png') # update image
	flute = pygame.transform.scale(flute,(100,100)) # update to correct size
	
	tulip = pygame.image.load('by-the-glass-mini-infographic.png') # update image
	tulip = pygame.transform.scale(tulip,(100,100)) # update to correct size
	
	snifter = pygame.image.load('by-the-glass-mini-infographic.png') # update image
	snifter = pygame.transform.scale(snifter,(100,100)) # update to correct size
	
	goblet = pygame.image.load('by-the-glass-mini-infographic.png') # update image
	goblet = pygame.transform.scale(goblet,(100,100)) # update to correct size
	
	# Beer 1 Variables =========================================================================================================
	beer1name = "Autumn Amber Ale" # notes about length here
	beer1style = "American Amber Ale" # notes about length here
	beer1OG = "OG: 1.048 SG" # notes about layout here
	beer1ibu = "IBU: 13.6" # notes about layout here
	beer1abv = "4.8%/VOL" # notes about layout here
	beer1kcal = "158.8 kcal/12oz" # notes about layout here
	beer1notes = "Beer 1 Notes, that can go on and on and on" # notes about length here, or wrap text
	beer1glass = "Beer 1 Glass"
	beer1glasspic = pint # select from Beer Glass Variables
	#other pic for beer or backgroud

	
	# Beer 2 Variables =========================================================================================================
	beer2name = "Autumn Amber Ale" # notes about length here
	beer2style = "American Amber Ale" # notes about length here
	beer2OG = "OG: 1.048 SG" # notes about layout here
	beer2ibu = "IBU: 13.6" # notes about layout here
	beer2abv = "4.8%/VOL" # notes about layout here
	beer2kcal = "158.8 kcal/12oz" # notes about layout here
	beer2notes = "Beer 1 Notes, that can go on and on and on" # notes about length here, or wrap text
	
	#pic of glass to use, use variable to quickly say which glass to use
	#other pic for beer or backgroud

	
	# Beer 3 Variables =========================================================================================================
	beer3name = "Beer 1 Name" # notes about length here
	beer3style = "Beer 1 Style" # notes about length here
	beer3OG = "Beer 1 OG" # notes about layout here
	beer3ibu = "Beer 1 IBU" # notes about layout here
	beer3abv = "Beer 1 ABV" # notes about layout here
	beer3kcal = "Beer 1 kcal" # notes about layout here
	beer3notes = "Beer 1 Notes" # notes about length here, or wrap text
	
	#pic of glass to use, use variable to quickly say which glass to use
	#other pic for beer or backgroud
	
	
	# Beer 1 Details - Left Tap ================================================================================================
	
	#backgroud pic
	
	# Beer 1 Name
	screenfont = pygame.font.SysFont(None, 40) # need to determine font and size
	rendered = screenfont.render(beer1name,0,(80, 200, 100)) # need to determine font color
	screen.blit(rendered, (0, 0)) # need to determine where on screen
	
	# Beer 1 Style
	screenfont = pygame.font.SysFont(None, 20) # need to determine font size
	rendered = screenfont.render(beer1style,0,(80, 200, 100)) # need to determine font color
	screen.blit(rendered, (0, 20)) # need to determine where on screen
	
	# Beer 1 Original Gravity (OG)
	screenfont = pygame.font.SysFont(None, 20) # need to determine font size
	rendered = screenfont.render(beer1OG,0,(80, 200, 100)) # need to determine font color
	screen.blit(rendered, (0, 40)) # need to determine where on screen
	
	# Beer 1 International Bittering Units (IBU)
	screenfont = pygame.font.SysFont(None, 20) # need to determine font size
	rendered = screenfont.render(beer1ibu,0,(80, 200, 100)) # need to determine font color
	screen.blit(rendered, (0, 60)) # need to determine where on screen
	
	# Beer 1 Alcohol / Volume (ABV)
	screenfont = pygame.font.SysFont(None, 20) # need to determine font size
	rendered = screenfont.render(beer1abv,0,(80, 200, 100)) # need to determine font color
	screen.blit(rendered, (0, 80)) # need to determine where on screen
	
	# Beer 1 Calories (kcal) / 12oz
	screenfont = pygame.font.SysFont(None, 20) # need to determine font size
	rendered = screenfont.render(beer1kcal,0,(80, 200, 100)) # need to determine font color
	screen.blit(rendered, (0, 100)) # need to determine where on screen
	
	# Beer 1 Taste Notes
	screenfont = pygame.font.SysFont(None, 20) # need to determine font size
	rendered = screenfont.render(beer1notes,0,(80, 200, 100)) # need to determine font color
	screen.blit(rendered, (0, 120)) # need to determine where on screen	
	
	# Beer 1 Glass
	screenfont = pygame.font.SysFont(None, 20) # need to determine font size
	rendered = screenfont.render(beer1glass,0,(80, 200, 100)) # need to determine font color
	screen.blit(rendered, (0, 140)) # need to determine where on screen		
	screen.blit(beer1glasspic, (0, 160))
	
		
	# draw line between each beer
	
	
	# Beer 2 Details - Middle Tap ==============================================================================================

	
	# draw line between each beer
	
	# Beer 3 Details - Right Tap ===============================================================================================
	
	
	#somewhere, kegerator temp, current date/time
	
	
	
	
	# when empty keg flash background red for time then stop?  flash other colors at different points?
	pygame.display.update() # Display everything

	
# Main Never Ending Loop =======================================================================================================
while True:
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()
			
	renderThings(screen) # Update the screen