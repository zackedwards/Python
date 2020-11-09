#Author Zack Edwards
#Exam 1 section 3

#Question 9: Write a script that takes a character (i.e. a string of length 1) as 
#input from the user and returns Trueif it is a vowel, False otherwise. 
#A check on the length of the input string and its being alphabetical is required
char = input("Please enter a single alphabetical charcter: ")
if len(char) > 1: 
    print('Not a single character') #This checks if the input is a single character or not
else:
    char = char.lower() #This checks whether its a letter or not
if char.islower() == False:
    print('Not a letter of the alphabet')
else:
    if 'a' in char:
        print('This character is a vowel')  #This checks to see if its a vowel
    elif 'i' in char:
        print('This character is a vowel')
    elif 'e' in char:
        print('This character is a vowel')
    elif 'o' in char:
        print('This character is a vowel')
    elif 'u' in char:
        print('This character is a vowel')
    elif 'y' in char:
        print('This character is a vowel')
    else:
        print('This character is not a vowel') #if it doesnt pass as a vowel then it is a consonant

#Question 10. Write a script that calculates the average word length and longest word of a text stored in a file. Please note:
#	The name of the file is word_list.csv and it doesn’t need to be asked to the user (meaning the name will be in the code)
#	Assume that the file contains n records, each one composed by 1 word. Words can be present more than once, but only unique words need to be considered
#	A sample word_list.csv file is attached for testing
file = open ("word_list.csv", "r") #opens the file
data = [] #initializing sveral variables for use later on
aveleng = 0
longest = 0
longestword = 'pie'
for line in file: 
    parts = line.strip().split(',') #This breaks up the file into a list of words
    data.append(parts)
for n in data: #For each part of the list
    for i in n: #The word within that part
        aveleng = (len(i) + aveleng) / 2 #Find the average length
        if len(i) > longest:
            longest = len(i) #find the longest word
            longestword = i
print('The average length is: ', aveleng)
print('The longest word is ',longestword, ' which is ', longest, ' characters long')

#11.Write a script that takes a string as input from the user and prints a string where for every character 
# in the original, there are three characters (example: 'The' → 'TTThhheee'). [NOTE: no check of the user input is 
# required]
str = input('Please input anything: ')
def triple(str): #defining my function
    for i in str: #for each character
        yield i * 3 #multiply by three
result = ''.join(triple(str)) #This glues them all together
print(result)
