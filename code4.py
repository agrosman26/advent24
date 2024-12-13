#day 4
#find xmas in word search

#import stuff
import numpy as np
import re

#read in data
data_name = input('Which data? ')
data = open(data_name+'/'+data_name+'4.txt','r')
rows = data.readlines()
chars = []
for i in range(len(rows)):
    chars.append([rows[i][j] for j in range(len(rows[i]))])

#count instances
def count(char_list):
    '''
    counts number of xmas instances in a line of characters
    Input:
        char_list (array): list of characters
    Output:
        (int): number of instances of the string XMAS
    '''
    line = ''.join(char_list)
    
    num_xmas = len(re.findall('XMAS',line))
    num_samx = len(re.findall('SAMX',line))
    
    return num_xmas+num_samx

down_chars = np.delete(np.transpose(chars),-1,0)

across_chars = np.transpose(down_chars)

count_xmas = 0
'''
#across
for i in range(len(across_chars)):
    #print(chars[i])
    this_count = count(across_chars[i])
    #print(this_count)
    count_xmas += this_count

#down
for i in range(len(down_chars)):
    #print(down_chars[i])
    this_count = count(down_chars[i])
    #print(this_count)
    count_xmas += this_count

#diagonal top to bottom
#print(down_chars)
diag = np.diagonal(across_chars)
this_count = count(diag)
count_xmas += this_count
diag = np.fliplr(across_chars).diagonal()
this_count = count(diag)
count_xmas += this_count
for i in range(1,len(across_chars)):
    diag = np.diagonal(across_chars,i)
    #print(diag)
    this_count = count(diag)
    #print(this_count)
    count_xmas += this_count
    diag = np.diagonal(across_chars,-i)
    #print(diag)
    this_count = count(diag)
    #print(this_count)
    count_xmas += this_count
    diag = np.fliplr(across_chars).diagonal(i)
    #print(diag)
    this_count = count(diag)
    count_xmas += this_count
    diag = np.fliplr(across_chars).diagonal(-i)
    #print(diag)
    this_count = count(diag)
    count_xmas += this_count
'''

def check_x(char_list):
    '''
    checks if the 3x3 array has an mas x
    Input:
        char_list (array): 3x3 array of characters
    Output:
        (boolean): true or false
    '''
    diag1 = ''.join(np.diagonal(char_list))
    diag2 = ''.join(np.fliplr(char_list).diagonal())
    #print(diag1,diag2)
    
    if diag1 == 'MAS' or diag1 == 'SAM':
        check_1 = True
    else:
        check_1 = False
        #print(diag1)
    if diag2 == 'MAS' or diag2 == 'SAM':
        check_2 = True
    else:
        check_2 = False
        #print(diag2)
    #print(check_1,check_2)
    return check_1 and check_2
    

count_x = 0
for i in range(len(across_chars)-2):
    for j in range(len(across_chars[i])-2):
        char_list = [[across_chars[i][j],across_chars[i][j+1],across_chars[i][j+2]],
                     [across_chars[i+1][j],across_chars[i+1][j+1],across_chars[i+1][j+2]],
                     [across_chars[i+2][j],across_chars[i+2][j+1],across_chars[i+2][j+2]]]
        if check_x(char_list):
            count_x += 1

print(count_xmas)
print(count_x)