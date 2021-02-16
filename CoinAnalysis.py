#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from Random import Random

# main function for our coin toss Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)
    # default single coin-toss probability for hypothesis 0
    p0 = 0.5

    # default single coin-toss probability for hypothesis 1
    p1 = 0.9

    haveH0 = False
    haveH1 = False

    if '-prob0' in sys.argv:
        p = sys.argv.index('-prob0')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            p0 = ptemp
    if '-prob1' in sys.argv:
        p = sys.argv.index('-prob1')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            p1 = ptemp
    if '-input0' in sys.argv:
        p = sys.argv.index('-input0')
        InputFile0 = sys.argv[p+1]
        haveH0 = True
    if '-input1' in sys.argv:
        p = sys.argv.index('-input1')
        InputFile1 = sys.argv[p+1]
        haveH1 = True
    if '-h' in sys.argv or '--help' in sys.argv or not haveH0:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("   -input0 [filename]  name of file for H0 data")
        print ("   -input1 [filename]  name of file for H1 data")
        print ("   -prob0 [number]     probability of 1 for single toss for H0")
        print ("   -prob1 [number]     probability of 1 for single toss for H1")
        print
        sys.exit(1)
    
    Ntoss = 1
    Npass0 = []
    LogLikeRatio0 = []
    Npass1 = []
    LogLikeRatio1 = []

    Npass_min = 1e5
    Npass_max = -1e5
    LLR_min = 1e5
    LLR_max = -1e5

data=np.genfromtxt(InputFile0,dtype=int)[:]
results=[]
for i in range(len(data)):
    a=0
    for l in range(len(data[i])):
        a+= data[i][l]
    results.append(a)

#Compute stats of results
mean=0
stdev=0
for i in range(len(results)):
    mean+=results[0]
mean= mean/len(results)

for i in range(len(results)):
    stdev+=(mean-results[i])**2
stdev = (stdev)**(1/2)/len(results)

print("For an experiment with ",len(data[0])," tosses after",len(results)," Experiments the mean amount of heads and stdev of that mean are: ",mean,stdev )
    

lab = str("sigma = "+str(stdev) + "  mean = " +str(mean))
plt.title( "Amount of experiments with (x) heads after "+str(len(results))+ " experiments" )


plt.hist(results,70,color="green",label=lab)
plt.legend(loc=1)
#plt.legend("sigma = "+str(stdev) + "mean = " +str(mean))
plt.show()
    
    
    
