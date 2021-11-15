from primzahlen import ist_primzahl

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
	zerlegung = []
	primFaktoren = primFaktoren(n)
	for p in primFaktoren:
		while(primFaktoren(p)!=[]:
			pass


#print(primZahlenVonBis(1,52))
print(primFaktoren(8))