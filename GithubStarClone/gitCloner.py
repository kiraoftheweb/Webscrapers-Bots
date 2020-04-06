import os
import re
import time

f = open("starred.txt")

for line in f:
    author = line.split("/")[3]
    filename = line.split("/")[4]
    final = author.strip("\n") + '-' + filename.strip("\n")
    #os.mkdir(final)
    os.system(f"git clone {line}")