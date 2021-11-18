# -*- coding: UTF-8 -*- 
from itertools import product
import time
from dukeHashv2 import hash
 
def bruteforce():
 
    nonce = "zzzz"
    nonceHash = hash(nonce)
    chars = 'ABCDEFGHIJKLMOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' # chars to look for
    attempts = 0
 
    t0 = time.time()
    t3 = t0
    rate = 0
    mins = 0
    hrs = 0
 
    for length in range(1, len(nonce) + 1): # only do lengths of 1 + 2
        to_attempt = product(chars, repeat=length)
        t1 = time.time()
        oldAttempts = attempts
        stamp = round(t1-t3)
        for attempt in to_attempt:
            if(hash(''.join(attempt)) == nonceHash):
                t1 = time.time()
                total = t1-t0
                print ("Versuche: " + str(attempts) + " Nonce: " + ''.join(attempt) + " Zeit: " + str(total), end="\r")
                return
            attempts = attempts + 1
            t1 = time.time()
            stamp2 = round(t1-t3)
            if(stamp2 > stamp):
                t3 = time.time()
                rate = (attempts - oldAttempts)*2
                oldAttempts = attempts
            sek = round(t1-t0)
            #if(sek > 60):
                #mins += 1
                #sek = 0
                #if(mins > 60):
                    #hrs += 1
                    #mins = 0
                    #sek = 0
            #if(mins == 0):
            times = str(sek)+"s"
            #elif(hrs == 0 and not mins == 0):
                #times = str(mins)+"m "+str(sek)+"s"
            #else:
                #times = str(hrs)+"h "+str(mins)+"m "+str(sek)+"s"
            print(hash(''.join(attempt))+" Versuche: "+str(attempts)+" Zeit: "+str(times)+" Hashrate: "+str(rate)+"H/s", end="\r")
 
    t1 = time.time()
    total = t1-t0
 
    print("Nonce nicht gefunden. Versuche: " + str(attempts))
 
bruteforce()