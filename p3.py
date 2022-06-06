s = "%s ma %s"
print(s % ('Ala', 'kota'))
print(s % ('Ala', 2.0))

print("%d %s o łącznym polu %f" % (2, "kwadraty", 4567.891011))
print("%d %s o łącznym polu %e" % (2, "kwadraty", 4567.891011))

print("|%20s|%-20s|" % ('Hello', 'Hello'))
print("|%20.3f|%-20.3f|" % (4567.891011, 4567.891011))

#################
print('#'*40)

s='{} ma {}'
print(s.format('Ala', 'kota'))
s='{1} {jakie} {0}'
print(s.format('koty', 2, jakie='duże'))
s='{1[0]} {slownik[a]}'
print(s.format('a', [5,6], slownik={"a":1}))

print("|{0:<20s}|{0:^20s}|{0:>20s}|".format('Hello'))
print("|{0:_<20s}|{0:+^20s}|{0:*>20s}|".format('Hello'))
print("|{0:_<20.1f}|{0:+^20.2f}|{0:*>20.3f}|".format(3456.13952))

###################

x = 1
y = 2
a = "Ala ma kota"
s = f"{x} {y} {(-2)**.5} Ala ma {a.split()[-1]}"
print(s)
