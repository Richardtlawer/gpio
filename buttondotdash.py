from gpiozero import LED, Button
from signal import pause
from time import sleep

led = LED(17)
button = Button(2)





def dot():
        led.on()
        sleep(0.5)
        led.off()
        sleep(1)

def dash():
        led.on()
        sleep(1)
        led.off()
        sleep(1)
        
def A():
    dot()
    dash()

def B():
    dash()
    dot()
    dot()
    dot()

def C():
    dash()
    dot()
    dash()
    dot()

def D():
   dash()
   dot()
   dot()

def I():
    dot()
    dot()

def H():
     dot()
     dot()
     dot()
     dot()

def R():
     dot()
     dash()
     dot()
def say_my_name():
     # button.when_pressed
      R()
      I()
      C()
      H()
      A()
      R()
      D()
button.when_pressed=say_my_name
#say_my_name()
pause()

