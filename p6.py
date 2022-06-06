x = input("Podaj liczbę: ")
#print(2*x)
try:
    y = 1/int(x)
except ValueError:
    print("To nie jest int")
except:
    print("Jakiś inny błąd")
else:
    print("Odwrotność", y)
    1/0 # błąd nie zablokuje finally2
finally:
    print("Wszystko czysto zamykam")