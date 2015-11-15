#!/bin/bash -ev

gcc -m64 -Werror -c -fmessage-length=0 -fno-stack-protector -fPIC -o"setflag.o" "setflag.c"
# gcc test2.c -L/home/surfvm-user/c/masterProjWS15/CTF/scripts/chilkat-9.5.0-x86-linux-gcc/lib -lchilkat-9.5.0 -lresolv -lpthread
g++ -g0 -m64 -L"/home/surfvm-user/c/masterProjWS15/CTF/scripts/chilkat-9.5.0-x86_64-linux-gcc/lib" ./setflag.o -osetflag -l"chilkat-9.5.0" -lpthread -lresolv

