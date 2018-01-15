#! /usr/bin/env python
import matplotlib.pyplot as plt
import main
import argparse
"""
this is the simulator of the network
shows a plot with the throughput of the network and the avg package delay for every possible value of p
shows a plot with the avg package delay and the values of p for each one of them
"""

parser = argparse.ArgumentParser()
parser.add_argument('-st','--simulationtime',help='the time in seconds for the simulation',type=int,default=10)
parser.add_argument('-ts','--timeslot',help='the actual time of a slot',type=float,default=0.01)
args = parser.parse_args()

if args.simulationtime < 0:
    raise ValueError('time interval needs to be a positive integer')
if args.timeslot < 0:
    raise ValueError('need to have a positive time slot')
st=args.simulationtime
ts=args.timeslot


#the matrix with all the possible values for p
chances = [0.1+0.1*i for i in range(10)]
#the sample with the total network delay for all possible values of p
sample = [main.main(SIM_TIME=st,CREATION_CHANCE=p,TIME_SLOT=ts)[0] for p in chances]
#all the network throughputs for the possible values of p
throughputs = [main.main(SIM_TIME=st,CREATION_CHANCE=p,TIME_SLOT=ts)[1] for p in chances]

#the plot for the p and total network delay
plt.subplot(2,1,1)
plt.plot(chances,sample,'ro')
plt.ylabel('avg pack delay')
plt.xlabel('p')
plt.axis([0,1.1,0,sample[-1]+2])

#the plot for the avg package delay and the throughputs for every possible p
plt.subplot(2,1,2)
plt.plot(throughputs,sample,'bo')
plt.ylabel('avg pack delay')
plt.xlabel('throughput')
plt.axis([throughputs[0]+0.1,throughputs[-1]+0.5,0,sample[-1]+1.5])

#show the plots
plt.show()

