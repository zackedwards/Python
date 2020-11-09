#Author Zack Edwards
#Ex5

import matplotlib.pyplot as plt

data = []
counts = [0,0,0,0,0,0]

def get_index(parts):
    for i in data:
        if 'NA' in i:
            continue
        if i[1] == '1':
            if '1' in i[0]:
                counts[0] += 1
            elif '2' in i[0]:
                counts[0] += 1
            elif '3' in i[0]:
                counts[0] += 1
            elif '4' in i[0]:
                counts[1] += 1
            elif '5' in i[0]:
                counts[1] += 1
            elif '6' in i[0]:
                counts[1] += 1
            else:
                counts[2] += 1
        elif i[1] == '2':
            if '1' in i[0]:
                counts[3] += 1
            elif '2' in i[0]:
                counts[3] += 1
            elif '3' in i[0]:
                counts[3] += 1
            elif '4' in i[0]:
                counts[4] += 1
            elif '5' in i[0]:
                counts[4] += 1
            elif '6' in i[0]:
                counts[4] += 1
            else:
                counts[5] += 1

marketingfile = open('marketingdata.txt', 'r')
for line in marketingfile:
    parts = line.strip().split()
    data.append(parts)
get_index(data)

print('Lower income males: ', counts[0],' Lower income females: ', counts[3])
print('Middle income males: ', counts[1],' Middle income females: ', counts[4])
print('Upper income males: ', counts[2], ' Upper income females: ', counts[5])

x=[1,2,3,4,5,6]
y=[counts[0],counts[1],counts[2],counts[3],counts[4],counts[5]]
plt.subplot(2,2,1)
plt.title('Bar graph of incomes')
plt.ylabel('Amount in group')
plt.xlabel('Income group')
plt.bar(x,y,)


plt.subplot(2,2,4)
plt.title('Pie chart of incomes')
labels = ['Lower income males','Middle income males','Upper income males','Lower income females','Middle income females','Upper income females']
plt.pie(counts, labels=labels)

plt.show()