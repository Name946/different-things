import glob
import re 
import sys
import os

directory = sys.argv[1]

for filename in glob.glob(directory + "/**/*", recursive=True):
    try:
        with open(filename, "r") as f:
            count = 0
            for line in f:
                match1 = re.findall(u"-", line)
                count+= len(match1)
        if count >= 1:
            os.remove(os.path.join(sys.path[0], filename))
    except IsADirectoryError:
        continue
