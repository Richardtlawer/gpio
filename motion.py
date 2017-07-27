from gpiozero import MotionSensor, LED
from signal import pause

pir = MotionSensor(4)
led = LED(17)

#pir.when_motion = led.on
#pir.when_no_motion = led.off

#pause()


#pir = MotionSensor(4)
while True:
    if pir.motion_detected:
        print("Motion detected!")
	
	pir.when_motion = led.on
	pir.when_no_motion = led.off

	pause()
