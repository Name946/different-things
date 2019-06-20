import glob, re, codecs, sys
import os
filename = sys.argv[1]

p = re.compile(u"=\n")
prod = re.compile(u">.*\n")


f = open(filename, "r")
result = ""
current = 0
for line in f:
    result += line;
    if re.match(prod, line):
        current += 1
    if re.match(p, line):
        f2 = codecs.open(filename+"__"+ str(current), "a", encoding="utf-8")
        f2.write(result)
        f2.close()
        current = 0
        result = ""
f.close()

my_dir = os.path.abspath(os.curdir) # cwd
usiversal_max = 0
for filename in glob.glob(my_dir + "/**/*", recursive=True):
    if "__" in filename:
        if int(filename.split("__")[-1]) > usiversal_max:
            usiversal_max = int(filename.split("__")[-1])

for filename in glob.glob(my_dir + "/**", recursive=True):
    if str(filename[-len(str(usiversal_max)):]) != str(usiversal_max):
        try:
            os.remove(filename)
        except IsADirectoryError:
            pass

             
