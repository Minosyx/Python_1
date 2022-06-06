f=open("plik.txt")
# try:
#     #printf(f.read())
#     print(f.read(10))
#     print(f.read(10))
# finally:
#     f.close()

with open("plik.txt") as f: # poprawny
    #printf(f.read())
    print(f.read(10))
    print(f.read(10))

with open("plik.txt", 'rb') as f: # poprawny
    #printf(f.read())
    print(f.read(10))
    print(f.read(10))

# with open("plik.txt", "a") as f:
#     f.write("\npies\n")

# with open("plik.txt", 'r+') as f:
#     print(f.read())
#     f.write("pies\n")

with open('b.txt', "w") as f:
    f.write('xx')

with open('plik.txt') as f:
    for linia in f:
        print(linia)

with open('plik.txt') as f:
    while True:
        x = f.readline()
        if not x:
            break
        print(x)