#!/usr/bin/python3
import cgi
from rawvalues import lightwrite as write



print("Content-type:text/html\n")
print("<HTML>")
print("<BODY>")
print("<h1> It Works! </h1>")
form = cgi.FieldStorage()
if form.getvalue("name"):
    name = form.getvalue("name")
    write(name)
print("<form method='post' action='index.py'>")
print("<p>Command: <input type='text' name='name'/></p>")
#print("<p>Temperature: " +temp+ "</p>")
print("<input type= 'submit' value='Submit' />")
print("</form>")
print("</BODY>")
print("</HTML>")
