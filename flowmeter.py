# File Name: flowmeter.py
# Created By: Kayser-Sosa, with help from ThatGuyYouKnow and JackBurtonn.
# Use: Displays information about the beers, how much is left in the kegs, date/time, and kegerator temperatures.

# Code modified from - Adafruit Kegomatic
# https://learn.adafruit.com/adafruit-keg-bot


# what can be removed from here?
# dont think beverage is needed, have to remove it from main as well
# getFormattedTotalPour - originally counted up, instead of down


# Imports ======================================================================================================================
import time
import random

class FlowMeter():
  PINTS_IN_A_LITER = 2.11338
  GAL_IN_A_LITER = 0.26417
  SECONDS_IN_A_MINUTE = 60
  MS_IN_A_SECOND = 1000.0
  displayFormat = 'gallon' # liter, gallon, pint
  beverage = 'beer'
  enabled = True
  clicks = 0
  lastClick = 0
  clickDelta = 0
  hertz = 0.0
  flow = 0 # in Liters per second
  #thisPour = 0.0 # in Liters
  totalPour = 0.0 # in Liters

  def __init__(self, displayFormat, beverage):
    self.displayFormat = displayFormat
    self.beverage = beverage
    self.clicks = 0
    self.lastClick = int(time.time() * FlowMeter.MS_IN_A_SECOND)
    self.clickDelta = 0
    self.hertz = 0.0
    self.flow = 0.0
    #self.thisPour = 0.0
    self.totalPour = 0.0
    self.enabled = True

  def update(self, currentTime):
    self.clicks += 1
	
    # get the time delta
    self.clickDelta = max((currentTime - self.lastClick), 1)
	
    # calculate the instantaneous speed
    if (self.enabled == True and self.clickDelta < 1000):
      self.hertz = FlowMeter.MS_IN_A_SECOND / self.clickDelta
      self.flow = self.hertz / (FlowMeter.SECONDS_IN_A_MINUTE * 7.5)  # In Liters per second
      instPour = self.flow * (self.clickDelta / FlowMeter.MS_IN_A_SECOND)  
      #self.thisPour += instPour
      self.totalPour -= instPour
	  
    # Update the last click
    self.lastClick = currentTime

 # def getBeverage(self):
 #   return str(random.choice(self.beverage))

 # def getFormattedClickDelta(self):
 #    return str(self.clickDelta) + ' ms'
  
 # def getFormattedHertz(self):
 #    return str(round(self.hertz,3)) + ' Hz'
  
 # def getFormattedFlow(self):
 #   if(self.displayFormat == 'liter'):
 #     return str(round(self.flow,3)) + ' L/s'
 #   elif(self.displayFormat == 'pint'):
 #	  return str(round(self.flow * FlowMeter.PINTS_IN_A_LITER, 3)) + ' pints/s'
 #   else:
 #	  return str(round(self.flow * FlowMeter.GAL_IN_A_LITER, 3)) + ' gal/s'
  
 # def getFormattedThisPour(self):
 #   if(self.displayFormat == 'liter'):
 #     return str(round(self.thisPour,3)) + ' L'
 #   elif(self.displayFormat == 'pint'):
 #     return str(round(self.thisPour * FlowMeter.PINTS_IN_A_LITER, 3)) + ' pints'
 #   else:
 #     return str(round(self.thisPour * FlowMeter.GAL_IN_A_LITER, 3)) + ' gal'
	  
  def getFormattedTotalPour(self):
#    if(self.displayFormat == 'liter'):
#      return str(18.927 - round(self.totalPour,3)) + ' / 18.927 L'
#    elif(self.displayFormat == 'pint'):
#      return str(40 - round(self.totalPour * FlowMeter.PINTS_IN_A_LITER, 3)) + ' / 40 pints'
#    else:
      #return str(10 - round(self.totalPour * FlowMeter.GAL_IN_A_LITER, 3)) + ' / 5.0 gal'   #old
	  return str(round(self.totalPour * FlowMeter.GAL_IN_A_LITER, 2))
	  
  def clear(self):
    #self.thisPour = 0;
    self.totalPour = 0;