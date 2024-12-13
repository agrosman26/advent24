#advent 2
#given list of reports
#each has levels
#safe if levels are gradually increasing or decreasing (differences between 1 and 3)
#unsafe if not

#import
import numpy as np
import pandas as pd

#read in data
data_name = input('Which data? ')
data = open(data_name+'/'+data_name+'2.txt','r')
reports = data.readlines()

#safe or unsafe?
def check(report,num):
    print('\n\n',report)
    levels = [int(a) for a in report.split(' ')]
    bads = []
    if levels == sorted(levels):
        print('sorted')
    elif levels == sorted(levels,reverse=True):
        print('reverse sorted')
    else:
        print('unsorted')
        #print(levels,sorted(levels))
        sames1 = [1 if levels[i] == sorted(levels)[i] else 0 for i in range(len(levels))]
        sames2 = [1 if levels[i] == sorted(levels,reverse=True)[i] else 0 for i in range(len(levels))]
        #print(sames1)
        for i in range(len(sames1)):
            if sames1[i] == 0 or sames2[i] == 0:
                bads.append(i)
        #print(levels,sorted(levels,reverse=True))
        #print(sames2)
        
    for i in range(len(levels)-1):
        diff = np.abs(levels[i]-levels[i+1])
        if diff < 1 or diff > 3:
            print('wrong diff')
            #print(i+1)
            bads.append(i+1)
    if len(bads) == 0:
        return True
    elif num > 0:
        return False
    safe_list = []
    for i in range(len(levels)):
        new_levels = levels.copy()
        new_levels.pop(i)
        safe_list.append(check(' '.join([str(a) for a in new_levels]),num+1))
    if True in safe_list:
        return True

count = 0
for report in reports:
    if check(report,0):
        print('safe')
        count += 1
    else:
        print('unsafe')

print(count)