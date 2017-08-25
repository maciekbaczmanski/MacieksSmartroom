import RPi.GPIO as GPIO
def initialisation():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #pin p5
    GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #pin p6
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # pin p1
    GPIO.setup(17, GPIO.IN)#pin P0 // broken?
    GPIO.setup(22, GPIO.OUT) #pin p3
    GPIO.setup(23, GPIO.OUT) #pin p4
    GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #pin p2
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # pin p2
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # pin p2


def pinval(pinnmb):
    return GPIO.input(pinnmb)
def pinout(pinnmb, state):
    GPIO.output(pinnmb, state)
def event(nmb, func):
    GPIO.add_event_detect(nmb, GPIO.FALLING, callback=func)


#window GPIO 27  P2
#doors GPIO 18  P1
#relaylight GPIO 22  P3
#outersen GPIO 13 P23
#innersen GPIO 6  P24
#relaypwr GPIO 23 P4