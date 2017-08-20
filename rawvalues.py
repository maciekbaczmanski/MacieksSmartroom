def temp():
    file2 = open("temp.txt", "r")
    temper = file2.read()
    return temper
def lightread():
    file3 = open("light.txt", "r")
    light = file3.read()
    file3.close()
    return light
def lightwrite(text):
    file4 = open("light.txt", "w")
    file4.write(text)
    file4.close()