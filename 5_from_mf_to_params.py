import time
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from scipy.special import factorial
from scipy.stats import erlang
from scipy.stats import gamma
import matplotlib.pyplot as plt
import matplotlib
import glob
import os
import sys
import math
from datetime import datetime
from scipy.integrate import simps
from numpy import trapz

startTime = datetime.now()
matplotlib.style.use('ggplot')
np.seterr(over='ignore')

path = sys.argv[1] # !!!

par = [0.0, 0.1, 0.12, 0.14, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
#par = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
"""
par = []
my_count = 0.0
while my_count <= 1:
    par.append(my_count)
    my_count += 0.1
    my_count = int(my_count*100) / 100
print(par)
"""
"""
pars = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.0, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 9.0, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10.0]
"""
pars = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]

#pars = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
#pars = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0, 5.2, 5.4, 5.6, 5.8, 6.0, 6.2, 6.4, 6.6, 6.8, 7.0, 7.2, 7.4, 7.6, 7.8, 8.0, 8.2, 8.4, 8.6, 8.8, 9.0, 9.2, 9.4, 9.6, 9.8, 10.0]

"""
pars = []
my_count = 0
while my_count <= 20:
    pars.append(float('{:.1f}'.format(my_count)))
    my_count += 0.1
"""

def func(x,a,l):
    return ((a ** x) * np.exp(-a) / factorial(x) )*z + ((x / l)**(k-1)* np.exp(-x / l)*(1-z)) / (l * factorial(k-1))
# целое a

for filename in glob.glob(os.path.join(path, '*.txt')):
    name = filename.split("/")[-1]
    with open(filename,"r") as f: #might be some problems with "counter" in file
        mf = f.read()
        mf = eval(mf)
        c = 0
        ef = {}
        for val in mf:
            c += mf[val]
        for val in mf:
            ef[val] = mf[val] / c
        ready_lists = []
        for a in ef.values():
            ready_lists.append(a)
        # Compute the area using the composite trapezoidal rule.
        area = trapz(ready_lists, dx=1)
        true_area = area * 0.2
        whole_list = ready_lists.copy()
        while area > true_area:
            ready_lists.pop()
            area = trapz(ready_lists, dx=1)
        minX = len(ready_lists)
        while len(ready_lists) + 1 != len(whole_list):
            if whole_list != []:            
                whole_list.pop()
            else:
                break
        area_more = trapz(whole_list, dx=1)
        deltaX = (true_area - area) / (area_more - area)
        deltaX = round(deltaX, 2)
        true_X = deltaX + minX
        df = pd.Series(ef) \
            .to_frame('y')
        remember = 1100000000
        for z in par:
            for k in pars:
                popt, pcov = curve_fit(func, df.index, df['y'], maxfev=10**8)
                sq = sum(((func(df.index, popt[0], popt[1]) - df['y'])*10000 / len(df) )**2) # (f(xdata, *popt) - ydata)**2
                if sq < remember:
                    remember = sq
                    with open(name, "w", encoding="utf-8") as f5:
                        f5.write("name ={0} sq={1} z={2} k={3} a={4} l={5}".format(name,sq,z,k,popt[0],popt[1]))
                    plt.ylim(0,0.3)
                    plt.xlim(0,50)
                    plt.scatter(df.index, df['y'], color='orange') # scatter or loglog
                    plt.scatter(df.index, func(df.index, *popt))
                    y1, x1 = [0.000001, 0.1], [true_X, true_X]
                    plt.plot(x1, y1, marker = 'o')
                    plt.title("X = "+str(true_X))
                    #os.remove(name +'.png')
                    plt.savefig(name +'.png', format='png', dpi=100)
                    plt.draw()
                    plt.close("all")

print(str(datetime.now()-startTime))
"""
matplotlib.style.use('ggplot')
np.seterr(over='ignore')
def func(x,k,t):
    return (x**(k-1)* np.exp(-x*t)) / (factorial(k-1)*t**k) 

    #return ( (p**x)* np.exp(-p) / factorial(x) )*(1-z) + (z)*( (x**(k-1)* np.exp(-x*t)) / (factorial(k-1)*t**k) )
#return ((0.8 ** x) * np.exp(-0.8) / factorial(x) )*(z) + 1/(b*(factorial(a-1))*((x/b)**(a-1))*np.exp(-x/b))

#return ((0.8 ** x) * np.exp(-0.8) / factorial(x) )*b + ((10 ** x) * np.exp(-10) / factorial(x))*(1-b)

mf = {0: 391.5, 1: 321.5, 2: 192.0, 3: 160.5, 4: 121.5, 5: 109.5, 6: 74.5, 7: 84.5, 8: 79.5, 9: 62.5, 10: 50.0, 11: 54.5, 12: 42.0, 13: 38.5, 14: 30.0, 15: 32.0, 16: 29.0, 17: 25.0, 18: 23.0, 19: 18.0, 20: 20.5, 21: 20.0, 22: 11.5, 23: 13.0, 24: 14.5, 25: 10.5, 26: 9.5, 27: 6.0, 28: 10.5, 29: 6.0, 30: 3.0, 31: 2.5, 32: 4.0, 33: 4.0, 34: 3.0, 35: 4.0, 36: 2.0, 37: 1.0, 38: 2.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 0.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 0.0, 48: 1.0, 49: 1.5, 50: 2.0, 51: 1.0, 52: 1.0, 53: 1.5, 54: 0.0, 55: 0.0, 56: 0.0, 57: 0.0, 58: 0.0, 59: 0.0, 60: 1.0, 61: 0.0, 62: 1.0}

c = 0
ef = {}
for val in mf:
    c += mf[val]

for val in mf:
    ef[val] = mf[val] / c

df = pd.Series(ef) \
       .to_frame('y')

popt, pcov = curve_fit(func, df.index, df['y'], maxfev=10**8)

print('b :\t{0}\ne :\t{1}\n'.format(*tuple(popt)))
print(popt)
print(pcov)

plt.loglog(df.index, df['y'], color='orange')
plt.loglog(df.index, func(df.index, *popt))
plt.savefig('6_0.9_2900_loglog.png', format='png', dpi=100)
plt.ylim(0,1)
plt.show()
"""
