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
    s = wochentag(2021, 10, 3)
    #i = 2
    #while(i < int(months[monat - 1])):
    #if(wochentag(jahr, monat, i) == "Sonntag"):
        #s = s + 1
        #i = i + 1
    if(returnNames):
        return (months[monat - 1], names[monat - 1], jahr, s)
    else:
        return months[monat - 1]

#stundenlohn = float(input("Stundenlohn: "))
#tageslohn = stundenlohn * int(input("Tagesstundenzahl: "))
var = anzahl(int(input("Jahr: ")), int(input("Monat: ")), True)
#steuer = int(input("Steuersatz in Prozent: "))

#print("Bruttomonatslohn für " + str(var[1]) + " " + str(var[2]) + ": " + str(var[0] * tageslohn) + "€")

#print("Nettomonatslohn für " + str(var[1]) + " " + str(var[2]) + ": " + str(var[0] * tageslohn - (var[0] * tageslohn / 100 * steuer)) + "€")
print("Sonntage: " + str(var[3]))
#print(anzahl(2021, 2)[3])
#print(wochentag(2021, 2, 1))
