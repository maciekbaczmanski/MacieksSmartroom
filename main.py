import threading
import time
import GUI
import rawvalues as val
from humidity import hum as humi
from messaging import getmsg, msg
from pins import initialisation, pinout, pinval as pin, event
from temp import pressure, temp
from counter import readin, readout
GUI.initiali()
initialisation()
lightout = False
pwr = False
GUI.addlabel("nowy", "Welcome to MacieksRoom", "red", 0, 0, 4, 0)
GUI.label40("nowy")
GUI.addlabel2("temp", "error", 1, 0)
GUI.addlabel2("hum", "error", 1, 1)
GUI.addlabel2("pressure", "error", 2, 0)
GUI.addlabel2("people", "error", 2, 1)
GUI.addlabel2("Doors", "error", 3, 0)
GUI.addlabel2("Window", "error", 3, 1)
humold = "nope"
people = 1
boolin = True
boolout = True


def lgt(btn):
    global lightout
    lightout = not lightout
    pinout(22, lightout)


def lgt2():
    global lightout
    lightout = not lightout
    pinout(22, lightout)

def pwrpopup(btn):
    GUI.setlabel("nowy", "Are You sure?")
    GUI.buttonhide("Light")
    GUI.buttonhide("Power")
    GUI.buttonshow("YES")
    GUI.buttonshow("NO")

def pwrout(btn):
    global pwr
    pwr = not pwr
    pinout(23, pwr)
    GUI.setlabel("nowy", "Welcome to MacieksRoom")
    GUI.buttonhide("YES")
    GUI.buttonhide("NO")
    GUI.buttonshow("Light")
    GUI.buttonshow("Power")
def stopopup(btn):
    GUI.setlabel("nowy", "Welcome to MacieksRoom")
    GUI.buttonhide("YES")
    GUI.buttonhide("NO")
    GUI.buttonshow("Light")
    GUI.buttonshow("Power")
GUI.addbutton("Light", lgt, 4, 0)
GUI.addbutton("Power", pwrpopup, 4, 1)
GUI.addbutton("YES", pwrout, 4, 0)
GUI.addbutton("NO", stopopup, 4, 1)
GUI.buttonhide("YES")
GUI.buttonhide("NO")
# val.hum() lub val.temp() !!!


msg("SYSTEM STARTED")


def loop():
    global lightout, humold, newhum, people
    while True:
        GUI.setlabel("temp", temp())
        GUI.setlabel("people", people)
        humbool, hum = humi()
        if humbool:
            newhum = hum
        if humbool:
            GUI.setlabel("hum", hum)
        GUI.setlabel("pressure", pressure())
        if pin(18): #18
            GUI.setlabel("Doors", "Doors: Closed")
        else:
            GUI.setlabel("Doors", "Doors: Opened")
        if pin(27):
            GUI.setlabel("Window", "Window: Closed")
        else:
            GUI.setlabel("Window", "Window: Opened")
        if not pin(24):
            msg("FIRE")

        if not pin(25):
            msg("GAS")
        if val.lightread() == "lightoff" or val.lightread() == "Lightoff":
            lightout = True
            pinout(22, True)
        if val.lightread() == "lighton" or val.lightread() == "Lighton":
            lightout = False
            pinout(22, False)
        val.lightwrite("0")

        time.sleep(0.1)
def loop5():
    while True:
        global newhum, lightout
        message = getmsg()
        if lightout:
            light = "Light: OFF"
        else:
            light = "Light: ON"
        if pin(18):
            doors = "Doors: Closed"
        else:
            doors = "Doors: Opened"
        if pin(27):
            window = "Window: Closed"
        else:
            window = "Window: Opened"

        if(message == "Data" or message == "data"):
            datamsg = "Room data: \n"+temp()+"\n"+pressure()+"\n"+newhum+"\n"+light+"\n"+doors+"\n"+window+"\n"
            msg(datamsg)
        if(message== "lightoff" or message== "Lightoff" or message== "Light off" or message== "light off"):
            lightout = True
            pinout(22, True)
        if(message== "lighton" or message== "Lighton" or message== "Light on" or message== "light on"):
            lightout = False
            pinout(22, False)
        time.sleep(6)

def pplcounter():
    global boolin, boolout
    event(13,readin)
    event(6, readout)


t = threading.Thread(target=loop)
t.daemon = True
t.start()
t2 = threading.Thread(target=loop5)
t2.daemon = True
t2.start()
t3 = threading.Thread(target=pplcounter)
t3.daemon = True
t3.start()
GUI.startgui()
