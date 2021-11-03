import math

def hash(string, hashLen):
    
    byte = string.encode()
    bytes = ""
    for b in byte:
        bytes = bytes + str(b)
     
    newBytes = ""
    newByte = 0
    factor = 0    
              
    if(len(bytes) > 150):
        for i in bytes:
            factor = factor + int(i)
        for i in bytes:
            newByte = int(i) * factor
            newBytes = newBytes + str(newByte)
        bytes = str(newBytes)    

    if(len(bytes) < hashLen):
        while(len(bytes) < hashLen):
            lastChar = int(bytes[-5:-1])
            secLastChar = int(bytes[-9:-5])
            if(lastChar == 0):
                lastChar = int(bytes[0:4])
            if(secLastChar == 0):
                secLastChar = int(bytes[4:8])
            newChar = lastChar + secLastChar
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
    
    for block in blocks:
        checksum = 0
        for i in block:
            checksum = checksum + int(i)
        if(checksum < 1000):
            checksum = checksum + 1000
        blockHex = '{:03x}'.format(checksum)
        if(hash == None):
            hash = "duke" + str(hashLen) + "$" + str(blockHex)
        else:
            hash = hash + str(blockHex)
    
    print("Programm abgeschlossen")
    return hash
    
print(hash("uvnhresubtisuernguvgahuriegviperbvipsahreufbagifüaoerjfiojraegbbbbbbbirguireuiahhgurednsfruifhur4ffviwbubfhbslhdbviwevbeS", 512))
print(hash("uvnhresubtisuernguvgahuriegviperbvipsahreufbagifüaoerjfiojraegbbbbbbbirguireuiahhgurednsfruifhur4ffviwbubfhbslhdbviwevbes", 512))
print(hash("Hello World", 512))
print(hash("Hello World!", 512))