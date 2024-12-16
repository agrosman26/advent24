#day 7
#determine whether certain operands can be combined to make a certain result

#import stuff
import re
import numpy as np

#get data
data_name = input('Which data? ')
data = open(data_name+'/'+data_name+'7.txt','r')

data_lines = data.read().split('\n')

#allowed operators
allowed = ['+','*']

def can_make(result,nums):
    '''
    determines whether you can make the result using the numbers, 
    by multiplying the first few numbers, then adding the rest
    Inputs:
        result (int): what we want
        nums (array): operands
    Output:
        valid (boolean): whether this is possible
    '''
    min_res = sum(nums)
    max_res = np.prod(nums)

    valid_list = []
    if result < min_res or result > max_res:
        valid = False
        valid_list.append(valid)
        print(result,'is less than',min_res,'or is greater than',max_res)
    elif result == min_res or result == max_res:
        valid = True
        valid_list.append(valid)
        #print('yes')
    else:
        #print('maybe')
        
        #check if divisible by last number
        for b in range(len(nums)):
            i = len(nums) - b - 1
            to_sub = [nums[j] for j in range(len(nums)) if j>i]
            to_div = nums[i]
            to_check = (result-sum(to_sub))

            #print('checking if',to_check,'is divisible by',to_div)

            if to_check % to_div == 0:
                #print('divisible')
                print(to_check,'is divisible by',to_div)
                divided = to_check/to_div
                valid = can_make(divided,nums[:i])
                valid_list.append(valid)
            else:
                print(to_check,'is not divisible by',to_div)
    
    if True in valid_list:
        return True
    
    #print(result,nums,'\n')
    return False

total = 0
for line in data_lines:
    nums = re.findall(r'\d+',line)
    nums = [int(a) for a in nums]
    result = nums.pop(0)
    #print(result,nums)

    #print(can_make(result,nums),'\n')

    if can_make(result,nums):
        total += result
        print('\n')
    else:
        print(result,nums,'\n')

print(total)