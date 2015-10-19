#!/bin/env python
import md5

flag    = "flg000001"
inStr   = "00000"

print("Flag: \t\t" + flag)
print("Input: \t\t" + inStr)

m = md5.new()
m.update(flag)
hsh = m.hexdigest()
print("Hash: \t\t" + hsh)

def encrpyt(inStr, hsh):
    outStr  = ""
    cnt = 0
    for ch in inStr:
        if cnt == 32:
            cnt = 0
        #print(ch + ": " + str(ord(ch)))
        #print(hsh[cnt] + ": " + str(ord(hsh[cnt])))
        tmp = ord(ch)+int(hsh[cnt],16)
        #print("New Ord: " + str(tmp))
        newChar = chr(tmp)
        #print(newChar + " " + str(ord(newChar)))
        while ord(newChar) > ord("z"):
        #while not newChar.isalnum():
            tmp = ord(newChar)-26
            print("While not alnum: " + str(tmp))
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

print("encrpyted: \t" + encrpyt(inStr, hsh))
print(decrypt_to_hash(inStr, encrpyt(inStr, hsh)))
print(hsh)
