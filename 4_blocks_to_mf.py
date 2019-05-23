import subprocess, sys, glob, os
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime
startTime = datetime.now()

directory = sys.argv[1]

asms = [] # block for number of genomes
my_counter = 0
for filename in glob.glob(directory + "/**/*", recursive=True):
    if my_counter == 0:
        my_counter += 1 
        with open(filename,"r") as f:
            for line in f:
                if line[0] == ">":
                    asms.append(line)

n_genomes = len(asms)
print("number of genomes = {0}".format(n_genomes))

buff = []
right_list = []
realy_list = []
sum_n = 0

print(str(datetime.now()-startTime))

# comment here to close



counter_gen_numb = n_genomes
while counter_gen_numb > 0:
    sum_n += counter_gen_numb
    counter_gen_numb = counter_gen_numb -1

new_list = [ [i] for i in range(0,sum_n)]
for item in new_list:
    item.pop(0)


for filename in glob.glob(directory + "/**/*", recursive=True):
    c = 0
    f = open(filename, "r", encoding="utf-8")
    x = f.readlines()
    my_str = ''.join(x)
    final = my_str.split("=")
    if "\n" in final:
        final.remove("\n")
    if "" in final:
        final.remove("")
    f.close()
    for first in final:
        for second in final:
            if final.index(second) >= final.index(first): 
                with open("Doc", "w", encoding="utf-8") as f2:
                    f2.write(first + "\n" + second)
                process=subprocess.call(['snp-sites','-p','-o','Doc','Doc'])
                with open("Doc", "r", encoding="utf-8") as f3:
                    line = f3.readline()
                    new_list[c].append(int(line[1:5]))
                c += 1
                os.remove("Doc")
another_list = [Counter(thing) for thing in new_list]

print(str(datetime.now()-startTime))

e = [i for i in range(1,n_genomes + 1)]

for my_numb in e:
    while realy_list.count(my_numb) != my_numb:
        realy_list.append(my_numb)
realy_list.reverse()

# for many empty lists
many_lists = [ i for i in range(1,1000)]
for i in many_lists:
    exec("lis{0} = []".format(str(i)))

for k,j in enumerate(realy_list): # it was huge construction
    exec("lis" + str(n_genomes + 1 - j) + ".append(another_list[k])")

"""
no switch
"""

def foo(arr): 
    average = sum(arr) / len(arr)
    if len(arr) < 4:
        return arr
    else:
        if average - arr[0] > arr[-1] - average: 
            return arr[1:]  
        elif average - arr[0] < arr[-1] - average:  
            return arr[:-1]
        elif average - arr[0] == arr[-1] - average:
            return arr

print("*")
for i in range(1, n_genomes + 1):
    exec("print(\"lis{0} =\".format(i))".format(i))
    exec("print(lis{0})".format(i))
print("*")

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

for group in combinations(range(1,n_genomes+1), 2):
    f_t = [ [] for i in range(1000)]
    exec("exec1 = lis{0}[{1}].items()".format(str(group[0]), str(group[1] - group[0])))
    for i in exec1:
        f_t[i[0]].append(i[1])
    for k,el in enumerate(f_t):
        f_t[k] = sorted(el)

    fxd = []
    rdyList = {}
    for lisT in f_t:
        if lisT == []:
            fxd.append([0])
        else:
            fxd.append(foo(lisT))
    first_zero = fxd.index([0])
    while len(fxd) >= first_zero:
        fxd.pop()
    if len(fxd) < 2:
        # here we need alert
        print("problems in " + str(group[0])+" "+str(group[1]))
        print(fxd)
        fxd.append([1])
        fxd.append([1])  
    for k,el in enumerate(fxd):
        average = sum(el) / len(el)
        rdyList[k]= average
    thing = pd.Series(rdyList)
    with open(str(group[0])+" "+str(group[1])+".txt","w") as f:
        f.write(str(rdyList))

    plt.xlabel("Number of SNPs")
    plt.ylabel("Blocks with SNPs")
    #thing.plot
    thing.plot(x="thing.index", y="thing.values")
    plt.ylim(0,200)
    plt.xlim(0,100)
    plt.savefig("single double "+str(group[0])+" "+str(group[1])+'.png', format='png', dpi=100)
    plt.clf()

#triple = [[1,6,8],[1,4,5],[2,5,6],[3,4,8]]
#for group in triple:
"""
for group in combinations(range(1,n_genomes+1), 3):
    f_t = [ [] for i in range(1000)]
    exec("exec1 = lis{0}[{1}].items()".format(str(group[0]), str(group[1] - group[0])))
    for i in exec1:
        f_t[i[0]].append(i[1])
    exec("exec2 = lis{0}[{1}].items()".format(str(group[0]), str(group[2] - group[0])))
    for i in exec2:
        f_t[i[0]].append(i[1])
    exec("exec3 = lis{0}[{1}].items()".format(str(group[1]), str(group[2] - group[1])))
    for i in exec3:
        f_t[i[0]].append(i[1])
    for k,el in enumerate(f_t):
        if el == []:
            f_t[k].append(0)
    for k,el in enumerate(f_t):
        f_t[k] = sorted(el)

    fxd = []
    rdyList = {}
    for lisT in f_t:
        if lisT == []:
            fxd.append([0])
        else:
            fxd.append(foo(lisT))
    while fxd[-1] == [0] or (fxd[-2] == [0] and fxd[-3] == [0] and fxd[-5] == [0]):
        fxd.pop()
    fxd.pop()
    while fxd[-1] == [0]:
        fxd.pop()
    for k,el in enumerate(fxd):
        average = sum(el) / len(el)
        rdyList[k]= average
    thing = pd.Series(rdyList)
    with open(str(group[0])+" "+str(group[1])+" "+str(group[2])+".txt","w") as f:
        f.write(str(rdyList))

    plt.xlabel("Number of SNPs")
    plt.ylabel("Blocks with SNPs")
    
    thing.plot(x="thing.index", y="thing.values")
    plt.ylim(0,200)
    plt.xlim(0,100)
    plt.savefig("single triple "+str(group[0])+" "+str(group[1])+" "+str(group[2])+'.png', format='png', dpi=100)
    plt.clf()  
"""    
"""
for group in combinations(range(1,n_genomes+1), 4):
    f_t = [ [] for i in range(1000)]
    exec("exec2 = lis{0}[{1}].items()".format(str(group[0]), str(group[1] - group[0])))
    for i in exec2:
        f_t[i[0]].append(i[1])
    exec("exec3 = lis{0}[{1}].items()".format(str(group[0]), str(group[2] - group[0])))
    for i in exec3:
        f_t[i[0]].append(i[1])
    exec("exec4 = lis{0}[{1}].items()".format(str(group[0]), str(group[3] - group[0])))
    for i in exec4:
        f_t[i[0]].append(i[1])
    exec("exec5 = lis{0}[{1}].items()".format(str(group[1]), str(group[2] - group[1])))
    for i in exec5:
        f_t[i[0]].append(i[1])
    exec("exec6 = lis{0}[{1}].items()".format(str(group[1]), str(group[3] - group[1])))
    for i in exec6:
        f_t[i[0]].append(i[1])
    exec("exec7 = lis{0}[{1}].items()".format(str(group[1]), str(group[3] - group[2])))
    for i in exec7:
        f_t[i[0]].append(i[1])
    for k,el in enumerate(f_t):
        if el == []:
            f_t[k].append(0)
    for k,el in enumerate(f_t):
        f_t[k] = sorted(el)

    fxd = []
    rdyList = {}
    for lisT in f_t:
        if lisT == []:
            fxd.append([0])
        else:
            fxd.append(foo(lisT))
    while fxd[-1] == [0] or (fxd[-2] == [0] and fxd[-3] == [0] and fxd[-5] == [0]):
        fxd.pop()
    fxd.pop()
    while fxd[-1] == [0]:
        fxd.pop()
    for k,el in enumerate(fxd):
        average = sum(el) / len(el)
        rdyList[k]= average
    thing = pd.Series(rdyList)
    with open(str(group[0])+" "+str(group[1])+" "+str(group[2])+" "+str(group[3])+".txt","w") as f:
        f.write(str(rdyList))

    plt.xlabel("Number of SNPs")
    plt.ylabel("Blocks with SNPs")
    
    thing.plot(x="thing.index", y="thing.values")
    plt.ylim(0,200)
    plt.xlim(0,100)

    plt.savefig("single quadra "+str(group[0])+" "+str(group[1])+" "+str(group[2])+" "+str(group[3])+'.png', format='png', dpi=100)
    plt.clf() 
"""

print(str(datetime.now()-startTime))

