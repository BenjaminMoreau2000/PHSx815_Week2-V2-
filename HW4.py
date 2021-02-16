#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from MySort import MySort

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()

    times = Sorter.DefaultSort(times)
    times_avg = Sorter.DefaultSort(times_avg)
    # try some other methods! see how long they take
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)

    # ADD YOUR CODE TO PLOT times AND times_avg HERE

    #Compute stats of results
    mean=0
    stdev=0
    for i in range(len(times)):
        mean+=times[i]
    mean= mean/len(times)

    for i in range(len(times)):
        stdev+=(mean-times[i])**2
    stdev = (stdev)**(1/2)/len(times)

    print("For an experiment with ",len(times)," times the mean amount of time and the stdev of that mean are: ",mean,stdev )

    lab = str("sigma = "+str(stdev) + "  mean = " +str(mean))   
    plt.hist(times,70,color="red",label= lab)
    plt.legend(loc=1)

    
    plt.hist(times_avg,70,color="green")
    plt.title( "Amount of experiments with (x) time after "+str(len(times))+ " times measured" )
    plt.show()



'''

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
'''
