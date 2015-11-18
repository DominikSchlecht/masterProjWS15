#!/bin/env python
import md5
import random

flag    = "flg000001"
inStr   = "ABC00000000000000000000000000000"
ran     = ""
for _ in range(0, 32):
    ran += random.choice("0123456789abcdef")

m = md5.new()
m.update(flag)
hsh = m.hexdigest()

def encrypt(inStr, hsh):
    outStr  = ""
    cnt = 0
    for ch in inStr:
        if cnt == 32:
            cnt = 0
        newOrd = ord(ch)+int(hsh[cnt],16)
        if newOrd > ord("9") and newOrd < ord("a"):
            newOrd += ord("a")-ord("9")-1
        newChar = chr(newOrd)
        while ord(newChar) > ord("z"):
            tmp = ord(newChar)-26
            newChar = chr(ord(newChar)-26)
        outStr += newChar
        cnt += 1
    return outStr

def decrypt(inStr, enc):
    tmp = ""
    cnt = 0
    ret = ""
    for ch in inStr:
        #print("\n" + ch + ": " + str(ord(ch)))
        #print(enc[cnt] + ": " + str(ord(enc[cnt])))
        #print(hex((ord(enc[cnt]) - ord(ch))))
        ret += str(hex((ord(enc[cnt]) - ord(ch))%26))[2:]
        cnt += 1
    return ret

print("Private:")
print("\t Flag: \t\t\t" + flag)
print("\t Hash: \t\t\t" + hsh)
print("\t encry no rand: \t" + encrypt(inStr, hsh))
print("\t new encr str: \t\t" + encrypt(inStr, ran))

print("\nUser defined:")
print("\t Input: \t\t" + inStr)

print("\nPublic:")
print("\t Rand: \t\t\t" + ran)
print("\t encry w. rand: \t" + encrypt(encrypt(inStr, ran), hsh))

print("\nDecrypted:")
print("\t decrypted: \t\t" + decrypt(encrypt(inStr, ran), encrypt(encrypt(inStr, ran), hsh)))
