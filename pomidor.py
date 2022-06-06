l = ["Ala %s kot", "Robert Ku%srwica", "Hot 1%s6"]

l1 = list(map(lambda i: i.__mod__("pomidor"), l))
l2 = list("pomidor".__rmod__(i) for i in l)
l3 = list(map("pomidor".__rmod__, l))

print(l1)
print(l2)
print(l3)
