from primzahlen import ist_primzahl
import math

def primZahlenVonBis(anfang, ende):
	zahlen = []
	while(anfang <= ende):
		if(ist_primzahl(anfang)):
			zahlen.append(anfang)
		anfang = anfang + 1
	return zahlen

def erstePrimzahlen(n):
	zahlen = []
	primzahlen = 0
	i = 1
	while(primzahlen < n):
		if(ist_primzahl(i)):
			zahlen.append(i)
			primzahlen = primzahlen + 1
		i = i + 1
	return zahlen

def teilerMenge(n):
	teiler = []
	i = 1
	while(i <= n):
		if(n%i == 0):
			teiler.append(i)
		i = i + 1
	return teiler

def primFaktoren(n):
	teiler = teilerMenge(n)
	primFaktoren = []
	for t in teiler:
		if(ist_primzahl(t)):
			primFaktoren.append(t)
	return primFaktoren

def primFaktorZerlegung(n):
	run = True
	zerlegung = []
	if(ist_primzahl(n)):
		zerlegung.append(n)
		return zerlegung
	while(run):
		faktoren = primFaktoren(n)
		zerlegung.append(faktoren[0])
		n = n/faktoren[0]
		if(ist_primzahl(n)):
			zerlegung.append(math.ceil(n))
			run = False
			break
	return zerlegung

#print(primZahlenVonBis(1,52))
#print(primFaktoren(36))
#print(primFaktoren(10))
print(primFaktorZerlegung(24))
print(primFaktorZerlegung(36))
print(primFaktorZerlegung(42))
print(primFaktorZerlegung(17))
print(primFaktorZerlegung(26))
print(primFaktorZerlegung(984))