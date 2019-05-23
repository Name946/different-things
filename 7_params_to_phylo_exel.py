import sys
import glob
import os
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import pandas as pd


path = sys.argv[1] # !!!
"""
with open("resualt_" + path.split("/")[-1],"a") as my_file:
    out = csv.writer(my_file, delimiter=',',quoting=csv.QUOTE_ALL)
    out.writerow(["name","sq","z","k","a","l"])
"""
for filename in glob.glob(os.path.join(path, '*.txt')):
    with open(filename,"r") as f:
        f_str = f.read()
    s_str = f_str.split(".txt")[1] # [-1]
    my_str = s_str.split(" ")
    my_str[0] = f_str.split(".txt")[0] # 0 name
    my_str[0] = my_str[0].split("=")[1] 
    my_str[1] = str( round(float(my_str[1].split("=")[1]), 3) ) # 1 sq
    my_str[2] = str( round(float(my_str[2].split("=")[1]), 3) ) # 2 z
    my_str[3] = str( round(float(my_str[3].split("=")[1]), 3) ) # 3 k
    my_str[4] = str( round(float(my_str[4].split("=")[1]), 3) ) # 4 a
    my_str[5] = str( round(float(my_str[5].split("=")[1]), 3) ) # 5 l
    with open("resualt_" + path.split("/")[-1][:2],"a") as my_file:
        out = csv.writer(my_file, delimiter=',',quoting=csv.QUOTE_ALL)
        out.writerow(my_str)
"""
dates = []
values = {}

with open("resualt_" + path.split("/")[-1], newline = '') as f:
    matr = [] # matrix
    for row in csv.reader(f, delimiter = ',', quotechar = '"'):
        if row[0] != "name":
            values[row[0]] = row[1:]
            dates = row[0]
        else:
            pass
    df = pd.DataFrame(values) # df is so casual
    max_sq = 0
    max_z = 0
    max_k = 0
    max_a = 0
    max_l = 0
    for x in df.iloc[1]:
        if float(x) > max_z:
            max_z = float(x)
    for x in df.iloc[0]:
        if float(x) > max_sq:
            max_sq = float(x)
    for x in df.iloc[2]:
        if float(x) > max_k:
            max_k = float(x)
    for x in df.iloc[3]:
        if float(x) > max_a:
            max_a = float(x)
    for x in df.iloc[4]:
        if float(x) > max_l:
            max_l = float(x)

dpi = 80
fig = plt.figure(dpi = dpi)
mpl.rcParams.update({'font.size': 10})

plt.title(path.split("/")[-1])
plt.xlabel('"sq","z","k","a","l"')
plt.ylabel('Score')
ax = plt.axes()
ax.yaxis.grid(True)

for reg in values.keys(): # values[reg] [0 to 4] is params
    print(values[reg])
    values[reg][0] = float(values[reg][0]) / max_sq
    values[reg][1] = float(values[reg][1]) / max_z
    values[reg][2] = float(values[reg][2]) / max_k
    values[reg][3] = float(values[reg][3]) / max_a
    values[reg][4] = float(values[reg][4]) / max_l
    plt.plot([i for i in range(1,6)], values[reg], linestyle = 'solid', label = reg)

# ["sq","z","k","a","l"]
plt.legend(loc='upper right', frameon = False)
fig.savefig("resualt_" + path.split("/")[-1]+".png")
plt.clf()

"""
"""
    plt.xlabel("Number of SNPs")
    plt.ylabel("Blocks with SNPs")
    #t hing.plot
    thing.plot(x="thing.index", y="thing.values")
    plt.ylim(0,200)
    plt.xlim(0,100)
    plt.savefig("single double "+str(group[0])+" "+str(group[1])+'.png', format='png', dpi=100)
    plt.clf()
"""
