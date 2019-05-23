# -*- coding: utf-8 -*-
import re
import sys
filename = sys.argv[1]

p = re.compile(u"=") # end of big block
prod = re.compile(u">") # begining of small block
A = re.compile(u"A")
T = re.compile(u"T")
C = re.compile(u"C")
G = re.compile(u"G")
gap = re.compile(u"-")
abz = re.compile(u"\n")

f = open(filename, "r", encoding="utf-8")

abzats = 0
count = 0
block_number = 0
file_counter = 0
align = 0
buff = ""
for line in f:
    if re.match(p, line):
        block_number += 1
        file_counter = 0
        buff=""
        align = 0
    elif re.match(prod, line):
        file_counter = 0
        buff = ""
        align += 1
    elif (re.match(A, line) or re.match(C, line) or re.match(G, line) or re.match(T, line) or re.match(gap, line)):
        for c in line:
            buff += c
            if (len(buff) == 1012 and len(buff.split('\n')) == 13):
                f2 = open(str(block_number) + "_" + str(file_counter), "a", encoding="utf-8")
                f2.write("\n> " + str(align)+"_"+ str(block_number)+"_"+str(file_counter)+"\n")
                f2.write(buff)
                f2.write("\n=")
                f2.close()
                buff = ""
                count = 0
                file_counter += 1
            elif (len(buff) == 1013 and len(buff.split('\n')) == 14):
                f2 = open(str(block_number) + "_" + str(file_counter), "a", encoding="utf-8")
                f2.write("\n> " + str(align)+"_"+ str(block_number)+"_"+str(file_counter)+"\n")
                f2.write(buff)
                f2.write("\n=")
                f2.close()
                buff = ""
                count = 0
                file_counter += 1
            elif (len(buff) == 1014 and len(buff.split('\n')) == 15):
                f2 = open(str(block_number) + "_" + str(file_counter), "a", encoding="utf-8")
                f2.write("\n> " + str(align)+"_"+ str(block_number)+"_"+str(file_counter)+"\n")
                f2.write(buff)
                f2.write("\n=")
                f2.close()
                buff = ""
                count = 0
                file_counter += 1
            elif (len(buff) == 1015 and len(buff.split('\n')) == 16):
                f2 = open(str(block_number) + "_" + str(file_counter), "a", encoding="utf-8")
                f2.write("\n> " + str(align)+"_"+ str(block_number)+"_"+str(file_counter)+"\n")
                f2.write(buff)
                f2.write("\n=")
                f2.close()
                buff = ""
                count = 0
                file_counter += 1
                print("записал 1015 1015 1015")
f.close()


