#!/usr/bin/python
# Energymeter puls reader to MQTT for Raspberry PI
# by Anton Gustafsson
# 2013-09-20

import RPi.GPIO as GPIO
from time import gmtime, strftime, time, localtime, mktime, strptime
import json
import urllib2
import base64
from math import fabs
import os 

config = {
      'user': 'spsensors',
      'password': 'BuCSlvWpl8reZP3R',
      'server': 'livinglab.powerprojects.se:6984'
      }


#Functions
#Time
def CurrentTime():
	return strftime("%Y-%m-%d %H:%M:%S", localtime())


#Class
class EnergyLogger():

	def __init__(self):

		self.Factor = 1 # kWh per pulse
		self.Threshhold = 10.0
	
		self.LastTime = 0.0
		self.Counter = 0.0
		self.LastPeriod = 0.0
		self.Falling = 0.0
		self.LastPower = 0.0

		self.error_threshhold = 50000

		self.pulse_lenght = 0.080 
		self.pulse_lenght_max_dev = 0.0005

		self.pin = 23

		#Config
		self.config = {
		      'user': 'spsensors',
		      'password': 'BuCSlvWpl8reZP3R',
		      'server': 'livinglab.powerprojects.se:6984',
		      'database': 'ii'
		}


		GPIO.setmode(GPIO.BCM)

		# GPIO 23 set up as inputs, pulled up to avoid false detection.
		GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

		# when a falling or rising edge is detected on port 23, call callback2
		GPIO.add_event_detect(self.pin, GPIO.BOTH, callback=self.my_callback3, bouncetime=0)

		return



	# now we'll define two threaded callback functions
	# these will run in another thread when our events are detected
	
	def my_callback3(self,channel):
		self.falling = time()

		print "%s Motion detected" 

		os.system("mpg321 Evil.mp3")

		return

	

if __name__ == "__main__":

	print "Make sure you have a button connected so that when pressed"
	print "it will connect GPIO port 23 (pin 16) to GND (pin 6)\n"
	print "You will also need a second button connected so that when pressed"
	print "it will connect GPIO port 24 (pin 18) to 3V3 (pin 1)\n"
	print "You will also need a third button connected so that when pressed"
	print "it will connect GPIO port 17 (pin 11) to GND (pin 14)"
	#raw_input("Press Enter when ready\n>")

	Logger = EnergyLogger()

	try:
		while(1):
			raw_input("Press Enter to simulate pulse\n>")
			Logger.my_callback(1)

    		print "Waiting for rising edge on port 24"
    		GPIO.wait_for_edge(24, GPIO.RISING)
    		print "Rising edge detected on port 24. Here endeth the third lesson."

	except KeyboardInterrupt:
    		GPIO.cleanup()       # clean up GPIO on CTRL+C exit
	GPIO.cleanup()           # clean up GPIO on normal exit

