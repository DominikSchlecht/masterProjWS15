import os
import sys
import subprocess


OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

#BUFFER_SIZE = 4096

#clients = []


def Folkswagen_emissions():
    tmp = ""
    print("\n********************************************************")
    print("**************** Welcome to Folkswagen *****************")
    print("********************************************************")
    print("\n********************************************************")
    print("*                                                      *")
    print("* FFFFFFFFFFFFFFFFF  W               W               W *")
    print("* FF                  W             W W             W  *")
    print("* FF                   W           W   W           W   *")
    print("* FF                    W         W     W         W    *")
    print("* FFFFFFFFFFF            W       W       W       W     *")
    print("* FF                      W     W         W     W      *")
    print("* FF                       W   W           W   W       *")
    print("* FF                        W W             W W        *")
    print("* FF                         W               W         *")
    print("*                                                      *")
    print("********************************************************\n\n")

    translator = False
    addfzn = False
    decrypt = False

    numberplz = "Ey du Gradler gib a moi dei Fahrgsteinumma ei:\n"
    wordplz = "Welches bayrische Wort moechten sie wissen?\n"
    wrongnum = "\nDes is fei koa gscheide Numma du de** du dammischer...\n\nSollten sie aus dem Ausland kommen und kein Bayrisch\nsprechen koennen sie auch unseren Uebersetzer nutzen!\nGeben sie dafuer folgendes ein: \n\"I ko koa bayrisch\"\n"
    cake = "The cake is a lie!\n"
    quittrans = "Der Uebersetzer laesst sich mit exit oder quit beenden.\n"
    emission = "Dei Emissionwert der ist ned so guad schaust ma her: \n"
    newFZN = "Ey du Gradler gib a moi a naie Fahrgsteinumma ei ond an Abgaswert ei (Fahrgsteinumma Abgaswert):\n"
    decryptSth = "Mogst was entschluesseln?\n"

    print(numberplz)

    while 1:
        data = raw_input()
        #print "data: " + data
        if not data:
            #print((WARNING + "\n[-] Client %s disconnected nicely" % (str(addr[0])) + ENDC))
            break
        else:
            data = (str(data)).strip()
            if translator:
                if(data == "quit" or data == "exit"):
                    translator = False
                    print(numberplz)
                else:
                    if not "\"" in data:
                        r = execute_shell("../ro/uebersetzer \"" + data + "\"")
                        tmp = r.stdout.read()
                        print("\nDas Wort "+ tmp + " in deutsch.\n");
                    print(wordplz)
            elif addfzn:
                if(data == "quit" or data == "exit"):
                    addfzn = False
                    print(numberplz)
                else:
                    if not "\"" in data:
                        r = execute_shell("../ro/setflag " + data)
                        tmp = r.stdout.read()
                        print(tmp)
                        #print "after execute_shell()"
                    print(newFZN)
            elif decrypt:
                if(data == "quit" or data == "exit"):
                    decrypt = False
                    print(numberplz)
                else:
                    if not "\"" in data:
                        r = execute_shell("../ro/setflag -h " + data)  # TODO
                        tmp = r.stdout.read()
                        print(tmp)
                        #print "after execute_shell()"
                    print("\n" + decryptSth);
            elif(data == "quit" or data == "exit"):
                #print((WARNING + "\n[-] Client %s disconnected nicely" % (str(addr[0])) + ENDC))
                break
            elif(data == "help"):
                print(cake)
            elif(data == "I ko koa bayrisch"):
                translator = True
                print(quittrans)
                print(wordplz)
            elif(data == "addfzn"):
                print(newFZN)
                addfzn = True
            elif(data == "decrypt"):
                print(decryptSth)
                decrypt = True
            else:
            #elif(re.match(pattern, data)):
                if not "\"" in data:
                    r = execute_shell("../ro/abgaswerte \"" + data + "\"")
                    tmp = r.stdout.read()
                if tmp != "Na\n":
                    #print(tmp)
                    print(emission + tmp + "\n")
                else:
                    print(wrongnum)

def execute_shell(command, error=''):
    return subprocess.Popen(command, shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)

if __name__ == "__main__":
    Folkswagen_emissions()