import time
from pins import pinval as pin
def readin(whatever):
    global boolin, people
    old = False
    if boolin:
        boolin = False
        x=0
        while x<150:
            x=x+1
            new = pin(6)
            if (new == False and old == True):
                x = 150
                people = people + 1
            old = new
        time.sleep(0.01)
        boolin = True

def readout(whatever):
    global boolout, people
    old = False
    if boolout:
        boolout = False
        x = 0
        while x < 150:
            x = x + 1
            new = pin(13)
            if (new == False and old == True):
                x = 150
                people = people - 1
            old = new
            time.sleep(0.01)
        boolout = True