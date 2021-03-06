import math

def hash(string, *args):
    
    byte = string.encode()
    bytes = ""
    for b in byte:
        bytes = bytes + str(b)
     
    newBytes = ""
    newByte = 0
    factor = 0
              
    for i in bytes:
        factor = factor + int(i)
    for i in bytes:
        newByte = int(i) * factor
        factor = factor + newByte
        newBytes = newBytes + str(newByte)
    bytes = str(newBytes)
    #else:
        #if(len(args) == 0):
            #print("Warnung: Es wurde keine Bytelänge übergeben. Der Hashwert ist unter Umständen nicht kollisionssicher!")

    if(len(args) == 1):
        for arg in args:
            hashLen = arg
        if(type(hashLen) != type(factor)):
            return "Argument 2 muss eine Ganzzahl sein"
        customHash = True
    else:
        hashLen = len(bytes)
        while(hashLen%16 != 0):
            hashLen = hashLen + 1
        customHash = False

    if(len(bytes) < hashLen):
        while(len(bytes) < hashLen):
            if(len(bytes) < 3):
                lastChar = int(bytes[0])
            else:
                lastChar = int(bytes[-3:-1])
            if(lastChar == 0):
                if(len(bytes) < 2):
                    lastChar = int(bytes[-1])
                else:
                    lastChar = int(bytes[0:4])
            newChar = lastChar * factor
            for i in str(newChar):
                factor = factor + int(i)
            bytes = bytes + str(newChar)
    
    if(len(bytes) > hashLen):
        while(len(bytes) > hashLen):
            lastChar = int(bytes[-3:-1])
            secLastChar = int(bytes[-5:-3])
            if(lastChar == 0):
                lastChar = int(bytes[0:2])
            if(secLastChar == 0):
                secLastChar = int(bytes[2:4])
            if(lastChar > secLastChar):
                newChar = lastChar - secLastChar
            else:
                newChar = secLastChar - lastChar
            byteSub = bytes[-4:-1][::-1]
            bytes = bytes[::-1]
            bytes = bytes.replace(str(byteSub), str(newChar), 1)
            bytes = bytes[::-1]

    blockCount = math.ceil(hashLen / 16)
    blocks = []
    index = 0
    counter = 1
    
    while(index < hashLen):
        blocks.append(bytes[index:math.ceil(counter * blockCount)])
        index = index + blockCount
        counter = counter + 1
    
    hash = None
    
    primzahlen = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    
    c = 0
    
    for block in blocks:
        checksum = 0
        for i in block:
            checksum = checksum + int(i)
        if(checksum < 1000):
            checksum = checksum + 1000
        checksum = math.ceil(math.sqrt(math.sqrt(checksum*primzahlen[c])*checksum*factor))
        c += 1
        blockHex = '{:03x}'.format(checksum)
        if(hash == None):
            if(customHash == True):
                hash = "duke" + str(hashLen) + "$" + str(blockHex)
            else:
                hash = "duke$" + str(blockHex)
        else:
            hash = hash + str(blockHex)
    
    return hash
    
#print(hash("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"))
#print(hash("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"))
#print(hash("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"))
#print(hash("zzz", 512))
#print(hash("zzZ", 512))
#print(hash("zZz", 512))
#print(hash("Zzz", 512))
#print(hash("fx", 512))
#print(hash("zzzz"))
#print(hash("przz"))