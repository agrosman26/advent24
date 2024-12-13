#day 5
#determine if the ordering is followed
#find middle of all correct lines
#add up

#open files
data_name = input('Which data? ')
data = open(data_name+'/'+data_name+'5.txt','r')
data = data.read()
data_list = data.split('\n\n')
rules = data_list[0].split('\n')
lines = data_list[1].split('\n')     

print(rules)
print(lines)

befores = []
afters = []

for rule in rules:
    befores.append(rule.split('|')[0])
    afters.append(rule.split('|')[1])

rule_zip = zip(befores,afters)

total = 0
all_rules = []

for line in lines:
    these_rules = []
    correct = True
    pages = line.split(',')
    middle = pages[len(pages)//2]
    #print(lines.index(line))
    for i,page in enumerate(pages):
        if page in befores:
            inds_p = [i for i in range(len(befores)) if befores[i]==page]
            for ind_p in inds_p:
                if afters[ind_p] in pages:
                    ind = pages.index(afters[ind_p])
                    if ind < i:
                        #print('incorrect before:',ind_p,':',befores[ind_p],afters[ind_p])
                        correct = False
                    if rules[ind_p] not in these_rules:
                        these_rules.append(rules[ind_p])
        if page in afters:
            inds_p = [i for i in range(len(afters)) if afters[i]==page]
            for ind_p in inds_p:
                if befores[ind_p] in pages:
                    ind = pages.index(befores[ind_p])
                    if ind > i:
                        #print('incorrect after:',ind_p,':',befores[ind_p],afters[ind_p])
                        correct = False
                    if rules[ind_p] not in these_rules:
                        these_rules.append(rules[ind_p])
    if correct:
        total += int(middle)
    all_rules.append(these_rules)

def fix_line(line,rules):
    '''
    takes in an incorrect line and rearranges the pages so it is correct
    Input:
        line (array): original line
        rules (array): rules
    Output:
        new_line (array): rearranged line
    '''
    befores = []
    afters = []
    for rule in rules:
        befores.append(rule.split('|')[0])
        afters.append(rule.split('|')[1])
    
    rules_zip = zip(befores,afters)
    sorted_rules = sorted(rules_zip)

    #print(sorted_rules)
    for page in line:
        if page in befores and page in afters:
            #print(page)
            thresh = len(line)//2
            if befores.count(page) >= thresh and afters.count(page) >= thresh:
                #print(page)
                total = int(page)
    return total

print(total)
full_total = 0
for i in range(len(lines)):
    #print('line',i)
    full_total += fix_line(lines[i].split(','),all_rules[i])
    #print('')

print(full_total - total)