#advent 3
#long string of stuff
#find places where it is mul(xxx,xxx) and do that multiplication
#add all products together

import numpy as np
import pandas as pd
import re

#read in data
data_name = input('Which data? ')
file = open(data_name+'/'+data_name+'3.txt','r')
data = file.read()

#regex
do_form = r'do\(\)'
dont_form = r'don\'t\(\)'
do_or_dont_form = r'don?\'?t?\(\)'
reg_format = r'mul\(\d{1,3},\d{1,3}\)'

match_list = []

split_list = re.split(do_form,data)
print(split_list)

for i,ex in enumerate(split_list):
    #print('do!')
    split_again = re.split(dont_form,ex)
    todo = split_again[0]
    print(todo)
    matched = re.findall(reg_format,todo)
    print(matched)
    match_list = np.concatenate((match_list,matched))

total = 0
for mult in match_list:
    nums = re.findall(r'\d+',mult)
    #print(nums)
    prod = np.prod([int(a) for a in nums])
    total += prod

print(total)