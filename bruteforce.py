# -*- coding: UTF-8 -*-

from itertools import product
import time
from dukeHash import hash

def bruteforce():

    nonce = "jdfh"
    nonceHash = hash(nonce)
    chars = 'ABCDEFGHIJKLMOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' # chars to look for
    attempts = 0

    t0 = time.time()

    for length in range(1, len(nonce) + 1): # only do lengths of 1 + 2
        to_attempt = product(chars, repeat=length)
        for attempt in to_attempt:
            if(hash(''.join(attempt)) == nonceHash):
                t1 = time.time()
                total = t1-t0
                return ("Versuche: " + str(attempts) + " Nonce: " + ''.join(attempt) + " Zeit: " + str(total))
            print(hash(''.join(attempt)))
            attempts = attempts + 1

    t1 = time.time()
    total = t1-t0

    print("Nonce nicht gefunden. Versuche: " + str(attempts))

print(bruteforce())