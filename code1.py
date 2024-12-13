#advent 1
#calculate differences between two lists
#add up differences

#import libraries
import numpy as np
import pandas as pd

#read in data
data_name = input('Which data? ')
data = pd.read_fwf(data_name+'/'+data_name+'1.txt',header=None)

#lists
list_1 = np.asarray(data[0])
list_2 = np.asarray(data[1])

#sort lists
sorted_1 = np.sort(list_1)
sorted_2 = np.sort(list_2)

#difference
diff = np.abs(sorted_2 - sorted_1)
total_diff = np.sum(diff)

#count num times in list 2
total_sim = 0
for num in list_1:
    count = np.count_nonzero(list_2 == num)
    sim_ind = count*num
    total_sim += sim_ind

print(total_diff)
print(total_sim)