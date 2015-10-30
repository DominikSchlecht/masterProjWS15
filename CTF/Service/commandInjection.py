#!bin/env python
import os
import sys
import re

param = raw_input("Please enter something: ")
match = re.search(";|\||`|\$|<|>|-", param)

if match:
    print("Found CommandInjection")
    sys.exit()

os.system("echo " + param)
