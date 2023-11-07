import sys
from datetime import datetime
import matplotlib
matplotlib.use('GTK3Cairo')  # or 'GTK3Cairo'
import matplotlib.pyplot as plt
import time

def getstats(lines):
    prevtime = None
    deltas = []
    timesum = 0
    for line in lines:
        clocktime = line.split('.')[0]
        thistime =  datetime.strptime(line.strip(), '%H:%M:%S.%f')
        if prevtime:
            delta = thistime - prevtime
            deltas.append(delta.microseconds)
            timesum = timesum + delta.microseconds
            print(delta.microseconds)
        prevtime = thistime
    meantime = (timesum /1000000) / (len(lines) - 1)
    print(f'mean time between packages {meantime}s')
    return deltas    

def main():
    args = sys.argv[1:]
    print(args)
    with open(args[0]) as logfile:
        Lines = logfile.readlines()
        print(Lines[0])
        microseconddeltas = getstats(Lines)
        
        plt.hist(microseconddeltas, density=True, bins=30)  # density=False would make counts
        plt.ylabel('Probability')
        plt.xlabel('Data');
        plt.show()




if __name__ == "__main__":
    main()
