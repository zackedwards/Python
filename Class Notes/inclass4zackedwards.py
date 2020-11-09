#Author Zacke Edwards
#in class excercise 4

def is_numeric(value): #a function to check if an input is a variable
    try:
        int(value) #if its an integer it returns y for yes
        return ('y')
    except:
        return ('n')
        
def factorial(num): #a function to take the factorial
    if num == 0:
        return 1 # the factorial of 0 is 1
    else:
        return num * factorial(num - 1)

def calc(num_list): #a function to summate and multiply the inputs
    sum_num = 0
    mult_num = 1
    for elem in num_list:
        sum_num = sum_num + elem #adds the element to the total
        mult_num = mult_num * elem #multiplies the element to the total
    return sum_num, mult_num
    
numbers_list = []

c = 0
while c <= 2: #gathering the inputs
    print('\nPlease enter number ',c+1, 'out of 3')
    num_in = input('> ')
    if is_numeric(num_in) == 'y': 
        numbers_list.append(int(num_in)) #if the input is a number it gets added to the list
        c = c+1
    else:
        continue
print('The factorial of the first number is ', factorial(numbers_list[0])) #printing the factorial
sum_total, mult_total = calc(numbers_list)
print('The sum of the numbers is ',sum_total)
print('The multiplication of the numbers is ',mult_total)