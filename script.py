import copy
s = 'Ala ma kota'
print(s.split('a'))
print(s.split(' ',1))
print(s.rsplit(' ',1))
print(s.rsplit(' ',1)[-1])
l = ['Ala', 'ma', 'kota']
print(('__').join(l))

print(s.startswith('ala'))
print(s.endswith('kota'))
print('abc'.isalpha())
print('1234'.isdigit())
print('ab123'.isalnum())

print('|'+'    Ala    '.strip()+'|')
print(s.replace('a', 'X'))

#string methods

print('\n'+'#'*40+'\n')

print(r'\t\n') # r - raw ignoruje znak ucieczki
s = 'Ala\nma\nkota'
print(s)
s = """Ala
ma
kota
"""
print(s)
print("'Ala'")
print('"Ala"')
print("\"Ala\"")

print('\n'+'#'*40+'\n')

l = ['a', 3, -1]
l.append(1j) # najlepsza opcja, bo najszybsza
# l = l+[1j]
# l += [1j]
print(l)

print(l.pop())
print(l)

l.insert(1,-1)
print(l)
l.remove(-1)
print(l)

# list methods
print('\n'+'#'*40+'\n')

l1 = [1,2,3] # przypisujemy listę do l1
# l2 = l1 # płytka kopia, l2 wskazuje na ten sam obiekt
l2 = l1[:]
l3 = copy.deepcopy(l1)
l1[0] = -1 # zmienia obiekt 1 na -1, ale na obiekt, na który wskazuje l1 wskazuje również l2
print(l2)
print(l3)

l1 = [[1,2],3,4]
l2 = l1[:]
l1[0][1] = 5
print(l2) # problem powtarza się piętro głębiej

# problem płytkiej kopii
print('\n'+'#'*40+'\n')

print(1==2, 1!=2, 1>=2, 1<=2, 1<2 or 2<1, 1<2 and 2<1, not 1<2)
# (a or b) and not (a and b) - xor

a = -2
if a < 1:	# nagłówek bloku
	print("<1")	# ciało bloku
	if a < 0:
		print("<0")

a = 1
if a < 2:
	print("<2")
else:
	print(">=2")

a = 0
if a < 2:
	print("<2")
elif a < 3:
	print("<3")
else:
	print(">=4")
	
x = 1
print("nieujemne" if x > 0 else "ujemne")

lista_wartosci_logicznych = [True, True, False, True]
print(all(lista_wartosci_logicznych))
print(any(lista_wartosci_logicznych))
