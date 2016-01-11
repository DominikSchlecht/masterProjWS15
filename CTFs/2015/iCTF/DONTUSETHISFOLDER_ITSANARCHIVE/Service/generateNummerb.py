import csv
# Install over pip --install rstr
import rstr
import random

Fahrzeugtypenstring = ""
f = open("info/Fahrzeugtypen.csv", 'rt')
f2 = open("info/Fahrzeugnummern.csv", 'w')
try:
    reader = csv.reader(f)
    for row in reader:
        Fahrzeugtypenstring += str(row)[2:5] + "|"
finally:
    f.close()
Fahrzeugtypenstring = Fahrzeugtypenstring[:-1]
pattern =  "^(WVW|WV2|1VW|3VW|9BW|AAV)(ZZZ)?(" + Fahrzeugtypenstring + ")([ABCDEFGHJKLMNPRSTVWXY]|[0-9])([ABCDEFGHJKLMNPRSTUVWXYZ]|[0-9])[0-9]{6}$"
f2.write("Nummer;")
for i in range (0, 100):
    tmp = rstr.xeger(pattern)
    f2.write(tmp + ";" + str(random.randint(1, 10)) + "\n")
    print(tmp)
f2.close()
