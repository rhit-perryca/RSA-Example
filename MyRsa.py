import os
import random
import math
import PrimeFinder


class RSAObj:
    def __init__(self, pubKey, privKey, N):
        self.pubKey = pubKey
        self.privKey = privKey
        self.N = N

def checkPubKey(key, T):
    return PrimeFinder.isMillerRabinPassed(key) and key < T and math.gcd(key, T) == 1
def getPubKey(T):
    start = T - PrimeFinder.getBigPrime()
    if start % 2 == 0:
        start += 1
    while not checkPubKey(start, T):
        start += 2
    return start
def getPrivKey(pubKey, T):
    i = PrimeFinder.getBigPrime()
    while True:
        if (i * pubKey) % T == 1:
            return i
        i += 2
def stringToInt(string):
    bytes = string.encode("utf-8")
    return int.from_bytes(bytes, byteorder="big")
def intToString(num):
    bytes = num.to_bytes((num.bit_length() + 7) // 8, byteorder="big")
    return bytes.decode("utf-8")
def getKeys():
    p = PrimeFinder.getBigPrime()
    q = PrimeFinder.getBigPrime()
    print("primes found")
    N = p * q
    T = (p - 1) * (q - 1)
    pub = getPubKey(T)
    print("Pub key found")
    priv = pow(pub, -1, T)
    print("Priv key found")
    return RSAObj(pub, priv, N)
def encrypt(msg, pubKey, N):
    msgInt = stringToInt(msg)
    return pow(msgInt, pubKey, N)
def decrypt(msg, privKey, N):
    msgInt = msg
    return intToString(pow(msgInt, privKey, N))
