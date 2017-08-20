from appJar import gui
app=gui()

def addlabel(title, message, bgcolor, row,col,c,d):
    app.addLabel(title, message,row,col,c,d)
    if not bgcolor == "":
        app.setLabelBg(title, bgcolor)

def addlabel2(title, message, row,col):
    app.addLabel(title, message,row,col)

def addlabel3(title, message, row,col,c,d):
    app.addLabel(title, message,row,col,c,d)


def setlabel(title, message):
    app.setLabel(title, message)

def addmessage(title, message,row,col):
    app.addMessage(title, message,row,col)

def setmessage(title, message):
    app.setMessage(title, message)

def warning(title, message):
    app.warningBox(title, message)


def addbutton(title, state,row,col):
    app.addButton(title, state,row,col)
def font(size):
    app.setFont(size, font=None)

def initiali():
    app.setFont("20", font=None)
    app.setButtonFont("40")
    app.setGeometry("fullscreen")
def setlabelwidth(name,width):
    app.setLabelWidth(name, width)
def label40(name):
    app.getLabelWidget(name).config(font=("Comic Sans", "40", "normal"))
def question(title, message):
    boolean = app.yesNoBox(title, message)
    return boolean
def buttonhide(name):
    app.hideButton(name)
def buttonshow(name):
    app.showButton(name)
def startgui():
    app.go()