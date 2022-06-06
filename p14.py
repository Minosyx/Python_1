import datetime

 # print(dir(datetime))

d = datetime.date(2002, 1, 12)
print(d)
d = datetime.date.today()
print(d.year, d.month, d.day)

t = datetime.datetime(2002, 1, 12, 3, 21, 2, 213)
print(t)
t = datetime.datetime.now()
print(t)
print(t.year, t.month, t.day, t.hour, t.minute, t.second, t.microsecond)
