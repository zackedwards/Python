#Author Zack Edwards
#Exam 1

#Question 6
x= 3
if 2 > x :
    print 'First print'
else :
    print 'Second'
    if 2 > x : #Not all parts of the code are relevant. The redundant code is: because if x is less than 2 then
        print 'Third' # it will already have printed ‘First print’ and not have moved on to the ‘else’ part of the code.
    print 'Fourth'#Also the code needs parentheses after the print statements around the desired message we want to print. 
print 'End'

#fixed version
x= 3
if 2 > x :
    print ('First print')
else :
    print ('Second')
    print ('Fourth')
print ('End')

#Question 7
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower,upper + 1):
if num > 1: #this line needs to be indented and every line after it to match
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
#answer
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower,upper + 1):
    if num > 1: #The only change I made was to indent this line, otherwise it worked fine
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)

#Question 8 
#Part A
#This code prints HELLO five times
# then prints GOOD-BYE
count = 0
while count < 5:
    print('HELLO')
print('GOOD-BYE')
#The problem here is that the counter stayes below 5 and is never modulated.
#fixed program:
count = 0
while count < 5:
    print('HELLO')
    count = count + 1
print('GOOD-BYE')
#Part B
# This code divides a number by 10 and prints the result as
#	a floating number, such as: 43.6
mynum = 436
print mynum/10 
#The problem here is that you need paranthesis around the subject of the print statement
mynum = 436
print(mynum/10)
#Part C
# This code will print ODD if the integer 
# innum is odd, otherwise it will print EVEN
invalue = raw_input('Type an integer number ')
innum = int(invalue)
if innum %2 == 0:
    print 'ODD'
else:
    print 'EVEN'
#Corrected code:
invalue = input('Type an integer number ')
innum = int(invalue)
if innum %2 == 0:
    print ('EVEN')
else:
    print ('ODD')
