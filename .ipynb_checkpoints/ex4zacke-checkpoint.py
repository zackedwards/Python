#Author Zack Edwards
#Excersize 4


def print_details(data):
    averagedailymiles = 0
    total24hour = 0
    for i in data:
        month = i[0][0]
        dailymiles = i[3]
        averagedailymiles = (float(averagedailymiles) + float(dailymiles)) / 2
        total24hour = (float(i[7])) + float(total24hour)
    print('\n')
    print('The following data is from ', data[0][0], ' to ', data[-1][0])
    print('\n')
    print('The average daily miles is ', averagedailymiles)
    print('\n')
    print('The total number of 24 hour passes aquired is ', total24hour)
    
    
file = open ("citi_bike.txt", "r")
data1 = []
for line in file:
    parts = line.strip().split()
    data1.append(parts)

print_details(data1)


file = open ("citi_bike.csv", "r")
data2 = []
for line in file:
    parts = line.strip().split(',')
    data2.append(parts)
    
print_details(data2)
    