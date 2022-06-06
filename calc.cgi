#!/usr/bin/python3

print('Content-type:text/html\n\n')

s = """<!DOCTYPE html><html><body>
<form method="get">
<input type="text" name="x">
+
<input type="text" name="y">
<input type="submit" value="=">
</form>
</body></html>"""

print(s)