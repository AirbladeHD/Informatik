import math

def ist_schaltjahr(jahr):
    if(jahr%400 == 0 or jahr%4 == 0 and jahr%100 != 0):
        return True
    else:
        return False
      
def anzahl_jahr(jahr):
    if(ist_schaltjahr(jahr)):
        return 366
    else:
        return 365
        
def anzahl(jahr, monat):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #names = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
    if(ist_schaltjahr(jahr)):
        months[1] = 29
    #return "Der Monat " + str(names[monat - 1]) + " im Jahr " + str(jahr) + " hat " + str(months[monat - 1]) + " Tage."
    return months[monat - 1]
    
def existenz(jahr, monat, tag):
   if(tag > anzahl(jahr, monat) or tag < 1):
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
    
def zeitlich_vor(jahr1, monat1, tag1, jahr2, monat2, tag2):
    if(jahr1 == jahr2 and monat1 == monat2 and tag1 ==  tag2):
        return "Die Daten sind gleich"
    if(jahr1 < jahr2):
        return "Das erste Datum liegt vor dem Zweiten"
    if(monat1 < monat2):
        return "Das erste Datum liegt vor dem Zweiten"
    if(tag1 < tag2):
        return "Das erste Datum liegt vor dem Zweiten"
    else:
       return "Das erste Datum liegt hinter dem Zweiten"
       
def folgetag(jahr, monat, tag):
    if(existenz(jahr, monat, tag) == False):
        return "Dieses Datum existiert nicht"
    if(tag + 1 > anzahl(jahr, monat)):
        if(not monat + 1 == 13):
            monat = monat + 1
            tag = 1
        else:
            monat = 1
            tag = 1
            jahr = jahr + 1
    else:
        tag = tag + 1
    return (jahr, monat, tag)

def jahreskalender(jahr):
    monat = 1
    tag = 1
    nextYear = jahr + 1
    while(jahr < nextYear):
        print(wochentag(jahr, monat, tag) + ", " + str(tag) + "." + str(monat) + "." + str(jahr))
        ft = folgetag(jahr, monat, tag)
        monat = ft[1]
        tag = ft[2]
        jahr = ft[0]
 
def ostersonntag(x):
    k = x/100
    m = 15 + (3*k + 3)/4 - (8*k + 13)/25
    s = 2 - (3*k + 3)/4
    a = x%19
    d = (19*a + m) % 30
    r = d/29 + (d/28 - d/29) * (a/11)
    og = 21 + d - r
    sz = 7 - (x + x / 4 + s)%7
    oe = 7 - (og - sz)%7
    os = og + oe
    if(1 <= os <= 31):
        return "Das Datum des Ostersonntags ist der " + str(math.floor(os)) + ". März"
    elif(os > 31):
        return "Das Datum des Ostersonntags ist der " + str(math.floor(os-31)) + ". April"

obst = ["Bananen","Birnen","Aprikosen"]

def istIn(list, element):
    if(element in list):
        return True
    else:
        return False

print(istIn(obst, "Bananen"))

#print(wochentag(2020, 11, 9))   
#jahreskalender(2021)
#print(folgetag(2000, 13, 21))
#print(ostersonntag(2024))