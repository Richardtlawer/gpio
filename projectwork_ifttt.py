from gpiozero import LED, Button
from time import sleep
from signal import pause
import urllib2

led=LED(17)
front_door_pressed=Button(2)
#def light():
#	  if(ifttt()==0):
#		front_door_pressed.when_pressed=ifttt
#		led.on()
#		sleep(2)
#		led.off()

def ifttt():
            print "done" 
      #led.on()
      #sleep(2)
      #led.off
            urllib2.urlopen("https://maker.ifttt.com/trigger/front_door_pressed/with/key/hBgwVN2raqAmjrPLQIULaTWbAejD8fYJipCyiKL3jlC").read

            front_door_pressed.when_pressed=ifttt
            led.on()
            sleep(2)
            led.off()

ifttt()
#light() 
pause()

