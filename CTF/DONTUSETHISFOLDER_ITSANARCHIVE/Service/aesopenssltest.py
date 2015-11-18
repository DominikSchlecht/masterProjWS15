import aesopenssl
data = "AAAAAAA\n" + ("%08x " * 8 + "\n")* 60
print(aesopenssl.translation(data))
