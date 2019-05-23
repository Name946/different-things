import sys
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import statistics as stat


path = sys.argv[1] # !!!

dates = []
values = {}

with open(path.split("/")[-1], newline = '') as f:
    for row in csv.reader(f, delimiter = ',', quotechar = '"'):
        if row[0] != "name":
            values[row[0]] = row[1:] # values are pre df
            dates = row[0]
        else:
            pass
    df = pd.DataFrame(values, index=['sq', 'z', 'k', 'a', 'l']) # df is so casual
    df = df.T
    dpi = 100
    mpl.rcParams.update({'font.size': 10})

    plt.title(path.split("/")[-1])
    plt.xlabel('"sq","z","k","a","l"')
    plt.ylabel('Score')
    ax = plt.axes()
    ax.yaxis.grid(True)
    
    sq_stat = []
    for el in df["sq"]:
        sq_stat.append(float(el))
    mean_sq = stat.mean(sq_stat)
    sigma_sq = stat.stdev(sq_stat)
    #variance(data)

    z_stat = []
    for el in df["z"]:
        z_stat.append(float(el))
    mean_z = stat.mean(z_stat)
    sigma_z = stat.stdev(z_stat)

    k_stat = []
    for el in df["k"]:
        k_stat.append(float(el))
    mean_k = stat.mean(k_stat)
    sigma_k = stat.stdev(k_stat)

    a_stat = []
    for el in df["a"]:
        a_stat.append(float(el))
    mean_a = stat.mean(a_stat)
    sigma_a = stat.stdev(a_stat)

    l_stat = []
    for el in df["l"]:
        l_stat.append(float(el))
    mean_l = stat.mean(l_stat)
    sigma_l = stat.stdev(l_stat)

    true_sq = sorted(df["sq"],key=float)
    print(true_sq)
    for s,E in enumerate(true_sq):
        for d,A in enumerate(range(1,len(df.index)+1)):
            if s == d:
                plt.title("M = {0} S = {1}".format(mean_sq,sigma_sq))
                plt.scatter(x=A, y=E, label = "sq")
    plt.savefig('sq.png', format='png', dpi=100)
    plt.clf()

    true_z = sorted(df["z"],key=float)
    print(true_z)
    for s,E in enumerate(true_z):
        for d,A in enumerate(range(1,len(df.index)+1)):
            if s == d:
                plt.title("M = {0} S = {1}".format(mean_z,sigma_z))
                plt.scatter(x=A, y=E, label = "z")
    plt.savefig('z.png', format='png', dpi=100)
    plt.clf()

    true_k = sorted(df["k"],key=float)
    print(true_k)
    for s,E in enumerate(true_k):
        for d,A in enumerate(range(1,len(df.index)+1)):
            if s == d:
                plt.title("M = {0} S = {1}".format(mean_k,sigma_k))
                plt.scatter(x=A, y=E, label = "k")
    plt.savefig('k.png', format='png', dpi=100)
    plt.clf()

    true_a = sorted(df["a"],key=float)
    print(true_a)
    for s,E in enumerate(true_a):
        for d,A in enumerate(range(1,len(df.index)+1)):
            if s == d:
                plt.title("M = {0} S = {1}".format(mean_a,sigma_a))
                plt.scatter(x=A, y=E, label = "a")
    plt.savefig('a.png', format='png', dpi=100)
    plt.clf()

    true_l = sorted(df["l"],key=float)
    print(true_l)
    for s,E in enumerate(true_l):
        for d,A in enumerate(range(1,len(df.index)+1)):
            if s == d:
                plt.title("M = {0} S = {1}".format(mean_l,sigma_l))
                plt.scatter(x=A, y=E, label = "l")
    plt.savefig('l.png', format='png', dpi=100)
    plt.clf()

"""
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

for reg in values.keys(): # round to 3
    values[reg][0] = str(round(float(values[reg][0]), 3))
    values[reg][1] = str(round(float(values[reg][1]), 3))
    values[reg][2] = str(round(float(values[reg][2]), 3))
    values[reg][3] = str(round(float(values[reg][3]), 3))
    values[reg][4] = str(round(float(values[reg][4]), 3))

for reg in values.keys(): # values[reg] [0 to 4] is params
    values[reg][0] = float(values[reg][0]) / max_sq # some standartisation
    values[reg][1] = float(values[reg][1]) / max_z
    values[reg][2] = float(values[reg][2]) / max_k
    values[reg][3] = float(values[reg][3]) / max_a
    values[reg][4] = float(values[reg][4]) / max_l
    plt.plot([i for i in range(1,6)], values[reg], linestyle = 'solid', label = reg) # plot vectors

# ["sq","z","k","a","l"]
plt.legend(loc='upper right', frameon = False)
fig.savefig("resualt_" + path.split("/")[-1]+".png")
plt.clf()


    plt.xlabel("Number of SNPs")
    plt.ylabel("Blocks with SNPs")
    #t hing.plot
    thing.plot(x="thing.index", y="thing.values")
    plt.ylim(0,200)
    plt.xlim(0,100)
    plt.savefig("single double "+str(group[0])+" "+str(group[1])+'.png', format='png', dpi=100)
    plt.clf()
"""
