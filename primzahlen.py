import math

def ist_primzahl(n):
	teilerGefunden = False
	if (n == 1 or n%2 == 0 and n != 2):
		teilerGefunden = True
	aktuelleZahl = 3
	while (aktuelleZahl <= math.sqrt(n) and not teilerGefunden):
		if (n % aktuelleZahl == 0):
			teilerGefunden = True
		aktuelleZahl = aktuelleZahl + 2
	return not teilerGefunden
