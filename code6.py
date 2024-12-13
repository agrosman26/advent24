#day 6
#map with # marking obstacles
#^,>,<,v marks a guard and their direction
#guard turns right at each obstacle
#count number of distinct location the guard gets to

import copy

#read in data
data_name = input('Which data? ')
data = open(data_name+'/'+data_name+'6.txt','r')
orig_data = data.read().split('\n')

for i,line in enumerate(orig_data):
    orig_data[i] = list(line)

guard_x = 0
guard_y = 0
guard_dir = 'right'

#get guard location and direction
for i,line in enumerate(orig_data):
    if '^' in line:
        guard_x = i
        guard_y = line.index('^')
        guard_dir = 'up'
    elif '<' in line:
        guard_x = i
        guard_y = line.index('<')
        guard_dir = 'left'
    elif '>' in line:
        guard_x = i
        guard_y = line.index('>')
        guard_dir = 'right'
    elif 'v' in line:
        guard_x = i
        guard_y = line.index('v')
        guard_dir = 'down'

#print(data)

for i,line in enumerate(orig_data):
    if '#' in line:
        ind = line.index('#')
        #print(i,ind)
        first = [i,ind]
        break

def add(area_map,extra=first):
    new_x = guard_x
    new_y = guard_y
    new_dir = guard_dir
    #move the guard around
    steps = []
    #print(len(data),len(data[0]))
    loop = True
    found = False
    data = copy.deepcopy(area_map)
    #print(data)
    data[extra[0]][extra[1]] = '#'
    while loop and not found:
        #print(guard_x,guard_y)
        data[new_x][new_y] = 'x'
        steps.append((new_x,new_y,new_dir))
        if new_dir == 'up':
            if new_x <= 0:
                #print('end')
                new_x -= 1
            else:
                ahead = data[new_x-1][new_y]
                if ahead == '#':
                    new_dir = 'right'
                else:
                    new_x -= 1
        elif new_dir == 'left':
            if new_y <= 0:
                #print('end')
                new_y -= 1
            else:
                ahead = data[new_x][new_y-1]
                if ahead == '#':
                    new_dir = 'up'
                else:
                    new_y -= 1
        elif new_dir == 'right':
            if new_y >= len(data[0])-1:
                #print('end')
                new_y += 1
            else:
                ahead = data[new_x][new_y+1]
                if ahead == '#':
                    new_dir = 'down'
                else:
                    new_y += 1
        elif new_dir == 'down':
            if new_x >= len(data)-1:
                #print('end')
                new_x += 1
            else:
                ahead = data[new_x+1][new_y]
                if ahead == '#':
                    new_dir = 'left'
                else:
                    new_x += 1
        if not(new_x in range(len(data)) and new_y in range(len(data[0]))):
            loop = False
        elif steps.count((new_x,new_y,new_dir)) > 1:
            found = True
            #print('loop!')
            print(extra)
    return found,data

total = 0
adds = 0

new_data = add(orig_data)[1]
#print(orig_data)
#print(new_data)

for i in range(len(new_data)):
    line = new_data[i]
    for j,space in enumerate(line):
        if space == 'x':
            #print(i,j)
            if add(new_data,[i,j])[0]:
                adds += 1
    num_x = line.count('x')
    total += num_x

print(adds)