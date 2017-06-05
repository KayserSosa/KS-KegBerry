# File Name: flowmeter.py
# Created By: Kayser-Sosa, with help from ThatGuyYouKnow and JackBurtonn.
# Use: Calculates the flow through the flow meters.

# Code modified from - Adafruit Kegomatic
# https://learn.adafruit.com/adafruit-keg-bot


# Imports ======================================================================================================================
import time
import random

# Classes ======================================================================================================================
class FlowMeter():
  PINTS_IN_A_LITER = 2.11338
  GAL_IN_A_LITER = 0.26417
  SECONDS_IN_A_MINUTE = 60
  MS_IN_A_SECOND = 1000.0
  displayFormat = 'gallon' # liter, gallon, pint
  enabled = True
  clicks = 0
  lastClick = 0
  clickDelta = 0
  hertz = 0.0
  flow = 0 # in Liters per second
  totalPour = 0.0 # in Liters

  # __init__ ====================================================================================================================
  def __init__(self, displayFormat):
    self.displayFormat = displayFormat
    self.clicks = 0
    self.lastClick = int(time.time() * FlowMeter.MS_IN_A_SECOND)
    self.clickDelta = 0
    self.hertz = 0.0
    self.flow = 0.0
    self.totalPour = 0.0
    self.enabled = True

  # update ======================================================================================================================
  def update(self, currentTime):
    self.clicks += 1
	
    # get the time delta
    self.clickDelta = max((currentTime - self.lastClick), 1)
	
    # calculate the instantaneous speed
    if (self.enabled == True and self.clickDelta < 1000):
      self.hertz = FlowMeter.MS_IN_A_SECOND / self.clickDelta
      self.flow = self.hertz / (FlowMeter.SECONDS_IN_A_MINUTE * 7.5)  # In Liters per second
      instPour = self.flow * (self.clickDelta / FlowMeter.MS_IN_A_SECOND)  
      self.totalPour -= instPour
	  
    # Update the last click
    self.lastClick = currentTime

  # getFormattedTotalPour =======================================================================================================	
  def getFormattedTotalPour(self):
	  return str(round(self.totalPour * FlowMeter.GAL_IN_A_LITER, 2))

  # clear =======================================================================================================================	  
  def clear(self):
    self.totalPour = 0;