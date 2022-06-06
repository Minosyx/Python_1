class Klasa:
    pass  # {} pusty blok


i1 = Klasa()
i2 = Klasa()

a = 2
i1.a = 3
i2.a = 4

print(a, i1.a, i2.a)

######################


class Klasa:
    """nasza klasa"""
    z = 10

    def metoda(*args):
        return args


print(Klasa.__doc__)

i1 = Klasa()
i2 = Klasa()

i1.z = 5

print(i1.z, i2.z)

print(i1.metoda('Ala', 1))
print(Klasa.metoda(i1, 'Ala', 1))

# instancja.metoda(*args) <=> Klasa.metoda(instancja, *args)

s = 'Ala123kot'

# print(''.join(filter(lambda i: str.isalpha(i), s)))
print(''.join(filter(str.isalpha, s)))
print(type('A'), 'A'.__class__)

########################


class Zwierze:
    def __init__(self, wiek, waga, imie):
        self.wiek = wiek
        self.waga = waga
        self.imie = imie


szczur = Zwierze(2.01, .51, "Paramaxil")

print(szczur.imie, szczur.wiek, szczur.waga)

#####################


class Nadrzedna:
    a = 2

    def metoda1(self):
        return self.a**2
    
    def metoda2(self):
        return 4*self.a


class Podrzedna(Nadrzedna):
    def metoda2(self):
        return 3*self.a


i1 = Podrzedna()

print(i1.metoda1())
print(i1.metoda2())
print(isinstance(i1, Nadrzedna), i1.__class__ == Podrzedna, type(i1) == Podrzedna)
print(isinstance(i1, Podrzedna), i1.__class__ == Nadrzedna, type(i1) == Nadrzedna)

############################


class Wektor:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x}; {self.y}]"
   
    def __add__(self, drugi):
        return Wektor(self.x + drugi.x, self.y + drugi.y)

    def __mul__(self, drugi):
        if isinstance(drugi, Wektor):
            return self.x * drugi.x + self.y * drugi.y
        else:
            return Wektor(self.x * drugi, self.y * drugi)      

    __rmul__ = __mul__

w = Wektor(1, 2)
u = Wektor(5, 4)
print(u+w+u)
print(w*u)
print(w*2)
print(2*w)
w *= 2
print(w)
print(int.__sub__(3, 4), int.__pow__(2, 3), int.__truediv__(11, 3), int.__mod__(11, 3), int.__floordiv__(11, 3), int.__divmod__(11, 3), int.__neg__(3))
print('abc'.__getitem__(1), 'abc'[1])
print(int.__ge__(3, 4)) # __ge__, __gt__, __lt__, __le__, __eq__, __ne__


class Forma(Wektor):
    def __call__(self, argument):
        return self * argument


f = Forma(-1, 4)
print(f(w))


class Wektor_int(Wektor):
    def __init__(self, *args):
        if not all([type(arg) == int for arg in args]):
            raise TypeError("Wszystkie współrzędne powinny być całkowite!")
        Wektor.__init__(self, *args)

    # przeciążyc __mul__

wi = Wektor_int(2, 4)
print(wi)

print(str.__mod__("Ala ma %s", "kota"))
print(list(map(lambda i: i**2, range(10))))
print(list(map((2).__rpow__, range(10))))
