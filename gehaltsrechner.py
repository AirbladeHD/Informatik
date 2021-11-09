import math

def ist_schaltjahr(jahr):
    if(jahr%400 == 0 or jahr%4 == 0 and jahr%100 != 0):
        return True
    else:
        return False

def anzahl(jahr, monat, returnNames):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    names = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
    if(ist_schaltjahr(jahr)):
        months[1] = 29
    if(returnNames):
        return (months[monat - 1], names[monat - 1], jahr)
    else:
        return months[monat - 1]

def existenz(jahr, monat, tag):
   if(tag > anzahl(jahr, monat, False) or tag < 1):
       return False
   else:
       return True

def wochentag(jahr, monat, tag):
    if(existenz(jahr, monat, tag) == False):
        return "Dieses Datum existiert nicht"
    kennzahlen = [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    tage = ["Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag"]
    if(ist_schaltjahr(jahr) == True):
        kennzahlen[0] = 5
        kennzahlen[1] = 1
    j = jahr % 100

    c = int(jahr/100)
    k = kennzahlen[monat - 1]
    d = tag + k + j + int(j/4) - 2 * (c%4)
    e = d%7
    return tage[e]

def freieTage(jahr, monat, weekend):
    tage = int(anzahl(jahr, monat, False))
    i = 1
    s = 0
    while(i < tage):
        if(weekend):
            if(wochentag(jahr, monat, i) == "Sonntag" or wochentag(jahr, monat, i) == "Samstag"):
                s = s + 1
        else:
            if(wochentag(jahr, monat, i) == "Sonntag"):
                s = s + 1
        i = i + 1
    return s

stundenlohn = float(input("Stundenlohn: "))
tageslohn = stundenlohn * int(input("Tagesstundenzahl: "))
jahr = int(input("Jahr: "))
monat = int(input("Monat: "))
samstag = False
if(input("Samstag freier Tag? Ja/Nein: ") == "Ja"):
    samstag = True
var = anzahl(jahr, monat, True)
steuer = int(input("Steuersatz in Prozent: "))

print("Bruttomonatslohn für " + str(var[1]) + " " + str(var[2]) + " ≈ " + str(math.ceil((var[0] - freieTage(jahr, monat, samstag)) * tageslohn)) + "€")

print("Nettomonatslohn für " + str(var[1]) + " " + str(var[2]) + " ≈ " + str(math.ceil((var[0] - freieTage(jahr, monat, samstag)) * tageslohn - (var[0] * tageslohn / 100 * steuer))) + "€")
