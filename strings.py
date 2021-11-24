# -*- coding: UTF-8 -*-

def zaehleBuchstaben(text, buchstabe):
	anzahl = 0
	for b in text:
		if(b == buchstabe):
			anzahl += 1
	return anzahl

def zaehleVokale(text):
	vok = 0
	vokale = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
	for b in text:
		if(b in vokale):
			vok += 1
	return vok

def ohneLeerzeichen(text):
	text = text.replace(' ', "_")
	return text

def strecke(text):
	text = ohneLeerzeichen(text)
	liste = []
	for b in text:
		liste.append(b)
	for e in liste:
		if(e != "_" and e != liste[len(liste)-1]):
			liste[liste.index(e)] = e+"_"
	text = ""
	for e in liste:
		text = text + e
	return text


print(strecke("Dies ist ein Test fuer die ohneLeerzeichen Funktion"))