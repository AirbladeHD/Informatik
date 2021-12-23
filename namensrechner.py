def NamensRechner(name1, name2):
    combined = name1.lower() + name2.lower()
    checked = []
    for l in combined:
        current = 0
        for c in combined:
            if(c == l):
                current += 1
        checked.append(current)
    if(not len(checked)%2 == 0):
        checked[0] = checked[0] + checked[-1]
        del checked[-1]
    while(len(checked) > 2):
        newList = []
        toCalc = len(checked)/2
        i = 0
        c = -1
        while(i < toCalc):
            val1 = checked[i]
            val2 = checked[c]
            newVal = val1 + val2
            if(newVal > 9):
                newVal = str(newVal)
                newList.append(int(newVal[0]))
                newList.append(int(newVal[1]))
            else:
                newList.append(newVal)
            i += 1
            c -= 1
        checked = newList
    toReturn = str(checked[0]) + str(checked[1])
    return toReturn
        
def SoulMate(name):
    names = ["Noah", "Leon", "Paul", "Matteo", "Ben", "Elias", "Finn", "Felix", "Henry", "Louis", "Manuel", "Ylenia", "Emilia", "Hannah", "Emma", "Sofia", "Mia", "Lina", "Mila", "Ella", "Lea", "Clara"]
    percent = []
    for n in names:
        percent.append([n, NamensRechner(name, n)])
    current = percent[0]
    for e in percent:
        if int(e[1]) > int(current[1]):
            current = e
    return "Dein Soulmate ist " + current[0] + " mit einer Übereinstimmung von " + current[1] + "%"

print(SoulMate("Ylenia"))
