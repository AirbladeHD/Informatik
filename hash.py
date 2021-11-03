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
    
print(hash("EJOULzthW6ftkabEtUYVMKSaDP9ozhW7zBBG8nW7lJpMjs6830SfFbXbwQA9RnFL3zIFOq1EsbIV6hhvOuP8bSPjQfzvzgNHKg736b4Y2i4mDhsh79Us7PZcyXASFSgLuVc19GF8IsarBhArjqxG1wPY3pnd4rEYgpHwSRWXFclCTXpFUU56IvFaGpapgkaE7a2UdOrj1ckUJAcIBzHPZzgNSfLnoCmGlV3sbLWINSi1bm0qRhnTSs0Uc8SdFmKdtCRHGXGde1I50EPLCtAwYlHXcaEF4yj6mc9D4kLgL7fJX6C1mFe1RpY1djfLikbWZku221CVmowPd6PHa4ysbazN015y6bGIv1LRPUQ0kxJsNHcVnyumykahaUx30Kr821rYj2oGPPJ2vyPRh9qSEAj21s3gdBg7isMtCKxi5auYUp0RAWxTXQjCufIm9q9BTe4UuiqZNjv7iaQzWcfxuawvarQOtElGhLLgDp6VJ7moDKWobMuHnN8G52dQZIdaoaDvc9mAvfm13iNtEHPpGgKmaU6ldyCmXBO2TfIzhIsDgyxTxHPlmAMqv76EK9x0q1vHlgqKXRsT3lEGO0xUo4P34MG3vIWQj9tTqCiQf4iMM8Cgp75WU56l67n6fuEbZsJgdoHC4h69D2yHJm92u9ngC5d3NPuVxFjLw1HazN8Hifa6Ia1ORpR71Gq1Cnc8o74kw50JTwAlP61AIuBgF4Cvl25ompVlLHHCLw798dRGvTJeTPx3jVi8vO1WbKHK8YNXLD8ZrhXwumpYqDHxvj8Co4FRd0nnhVfAZw6W15foo9ltqCYe1zb73amc6cuZWFYkdnTCNUsYuN8MxEAt3l2CJikOBUhZz3JiZZSKtnHVnOGJFkCMxw1rGVudJxTgQN0aC4QzrEjHvigoCWYVD9W49Ul3Tp84DactCLd2KoDeqyVy4TDaSYEi4a1uMeQEfF75goOTfta0wglQ1MPUVwqL9TUgLTDnYpIzRozJ", 512))
print(hash("EJOULzthW6ftkabEtUYVMKSaDP9ozhW7zBBG8nW7lJpMjs6830SfFbXbwQA9RnFL3zIFOq1EsbIV6hhvOuP8bSPjQfzvzgNHKg736b4Y2i4mDhsh79Us7PZcyXASFSgLuVc19GF8IsarBhArjqxG1wPY3pnd4rEYgpHwSRWXFclCTXpFUU56IvFaGpapgkaE7a2UdOrj1ckUJAcIBzHPZzgNSfLnoCmGlV3sbLWINSi1bm0qRhnTSs0Uc8SdFmKdtCRHGXGde1I50EPLCtAwYlHXcaEF4yj6mc9D4kLgL7fJX6C1mFe1RpY1djfLikbWZku221CVmowPd6PHa4ysbazN015y6bGIv1LRPUQ0kxJsNHcVnyumykahaUx30Kr821rYj2oGPPJ2vyPRh9qSEAj21s3gdBg7isMtCKxi5auYUp0RAWxTXQjCufIm9q9BTe4UuiqZNjv7iaQzWcfxuawvarQOtElGhLLgDp6VJ7moDKWobMuHnN8G52dQZIdaoaDvc9mAvfm13iNtEHPpGgKmaU6ldyCmXBO2TfIzhIsDgyxTxHPlmAMqv76EK9x0q1vHlgqKXRsT3lEGO0xUo4P34MG3vIWQj9tTqCiQf4iMM8Cgp75WU56l67n6fuEbZsJgdoHC4h69D2yHJm92u9ngC5d3NPuVxFjLw1HazN8Hifa6Ia1ORpR71Gq1Cnc8o74kw50JTwAlP61AIuBgF4Cvl25ompVlLHHCLw798dRGvTJeTPx3jVi8vO1WbKHK8YNXLD8ZrhXwumpYqDHxvj8Co4FRd0nnhVfAZw6W15foo9ltqCYe1zb73amc6cuZWFYkdnTCNUsYuN8MxEAt3l2CJikOBUhZz3JiZZSKtnHVnOGJFkCMxw1rGVudJxTgQN0aC4QzrEjHvigoCWYVD9W49Ul3Tp84DactCLd2KoDeqyVy4TDaSYEi4a1uMeQEfF75goOTfta0wglQ1MPUVwqL9TUgLTDnYpIzrozJ", 512))