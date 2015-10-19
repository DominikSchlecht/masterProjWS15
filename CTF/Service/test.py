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
        #print(ch + ": " + str(ord(ch)))
        #print(hsh[cnt] + ": " + str(ord(hsh[cnt])))
        newOrd = ord(ch)+int(hsh[cnt],16)
        if newOrd > ord("9") and newOrd < ord("a"):
            newOrd += ord("a")-ord("9")-1
        #print("New Ord: " + str(tmp))
        newChar = chr(newOrd)
        #print(newChar + " " + str(ord(newChar)))
        while ord(newChar) > ord("z"):
        #while not newChar.isalnum():
            tmp = ord(newChar)-26
            #print("While not alnum: " + str(tmp))
            newChar = chr(ord(newChar)-26)
        outStr += newChar
        cnt += 1
    return outStr

def decrypt_to_hash(inStr, outStr):
    tmp = ""
    cnt = 0
    hsh = ""
    for ch in inStr:
        hsh += str(hex((ord(outStr[cnt]) - ord(ch))%26))[2:]
        cnt += 1
    return hsh
print("Private:")
print("\t Flag: \t\t\t" + flag)
print("\t Hash: \t\t\t" + hsh)
print("\t encry no rand: \t" + encrypt(inStr, hsh))

print("\nUser defined:")
print("\t Input: \t\t" + inStr)

print("\nPublic:")
print("\t Rand: \t\t\t" + ran)
print("\t encry w. rand: \t" + encrypt(encrypt(inStr, ran), hsh))
