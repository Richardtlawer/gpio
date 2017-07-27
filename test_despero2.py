from gpiozero import LED, Button
from time import sleep
from signal import pause
import urllib2
from gpiozero import MotionSensor

led=LED(17)
front_door_pressed=Button(27)
pir = MotionSensor(4)


def onpress():
	pir.wait_for_motion(1)
	if pir.motion_detected:
		flashled()
		print("motion detected")
	else:
		ifttt()
	
def flashled():
	led.on()
	sleep(3)
	led.off()
	sleep(0)
        
def ifttt():
            print "No motion in room. sending mail" 
            urllib2.urlopen("https://maker.ifttt.com/trigger/front_door_pressed/with/key/hBgwVN2raqAmjrPLQIULaTWbAejD8fYJipCyiKL3jlC").read
            
front_door_pressed.when_pressed = onpress

	
pause()

