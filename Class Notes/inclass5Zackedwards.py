#Author Zack edwards
#in class excercise 5

import re

def validate(password):
    for i in password:
        if (len(i) < 6) or (len(i) > 12):
            continue
        if not re.search('[a-z]', i):
            continue
        if not re.search('[0-9]', i):
            continue
        if not re.search('[A-Z]', i):
            continue
        if not re.search('[$#@]', i):
            continue
        finalpass.append(i)
       
        
passw = input('Enter some passwords seperated by commas: ')
password = passw.split(',')
finalpass = []
validate(password)
print('The following are valid passwords')
print(*finalpass, sep = ', ')
if len(finalpass) == 0:
    print('No passwords worked')