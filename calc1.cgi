#!/usr/bin/python3

from cgi import FieldStorage

f = FieldStorage()

x = f.getfirst("x", '')
y = f.getfirst("y", '')

try:
    z = float(x) + float(y)
except:
    z = ''

print('Content-type:text/html\n\n')

s = """<!DOCTYPE html><html><body>
<form method="get">
<input type="text" name="x">
+
<input type="text" name="y">
<input type="submit" value="=">
%s
</form>
</body></html>""" % (z,)

print(s)
