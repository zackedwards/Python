#Author Zack Edwards

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
import nltk
import string

data = pd.read_csv('H_Clinton-emails.csv')
data = data.fillna(0)
data = data.dropna()
#data.head(20) #print the first 20 lines of the data
#data.tail() #print the last lines of the data


senders = data['ExtractedFrom'] #isolating the senders name and email
temp = [] #creating an empty temporary list
for i in senders: #a loop which eliminated 0's whoch occur from empty cells
    i = str(i) #interprettng each cell as a string
    if len(i) != 1: #by seeing i as a string we can see its length and get rid of entries with length of 1
        temp.append(i)
senders_list = temp
#print(senders_list[:20]) #printing one cell from the list of senders

sender_emails = [] #creating a list for the senders emails
for i in senders_list: #this loops will extract the emails
    i = i.strip().split()
    for x in i:
        if '<' in x:
            if '>' in x: #this grabs any word that contains both < and > 
                sender_emails.append(x) #and appends it to the list of emails
#print(sender_emails) #this prints the emails


frequency = [] #creating a list for the frequency each email appears
for w in sender_emails: #for each email in the list
    frequency.append(sender_emails.count(w)) #count the frequency each email appears
#print(frequency[:20]) #printing as a test
sender_and_frequency = list(zip(sender_emails, frequency))
#print(sender_and_frequency) #printing one example 


def removeDuplicates(lst): #creating a function to remove duplicates from a list of tuples
    return list(set([i for i in lst]))
def getKey(item): #creating a function to sort a list of tuples by the second item in the tuple
    return item[1]


top_15_senders = (removeDuplicates(sender_and_frequency)) #removing duplicate emails
top_15_senders = sorted(top_15_senders, key=getKey, reverse=True) #sorting by frequency


counter = 0
top_15_names = []
name = ''
for i in top_15_senders: #this loop finds the names for each sender
    for x in senders_list:
        if i[0] in x:
            L = len(i[0])
            name = x[:-len(i[0])]
        if name == 'H':
            name = 'Hillary Clinton'
    top_15_names.append(name)
    counter += 1
    if counter < 16:
        continue
    else:
        break


print('\nThese are the top 15 most frequent senders from the Clinton emails:')
counter = 0
for i in top_15_senders:
    print('Sender #', counter+1)
    print('Name: ', top_15_names[counter], '\nEmail: ', i[0], '\nFrequency: ', i[1], '\n')
    counter += 1
    if counter < 16:
        continue
    else:
        break
print('hrod17@clintonemail.com is the only email which in not an @state.gov, it is the ')
print('private email server which hillary infamously used to send classified information.')
print('Though the assignment was to print the top 15 correspondants I printed 16 since one was Hillary herself')
print('\nThis is a graph of the frequency of correspondance with the 15 most common senders (excluding Hillary)')
top_15_frequencies=[]
counter = 0
for i in top_15_senders:
    top_15_frequencies.append(i[1])
    counter += 1
    if counter < 16:
        continue
    else:
        break
#print(top_15_frequencies)
y= top_15_frequencies[1:]
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
plt.bar(x=x,height=y,data=y)
plt.xlabel('Senders 1-15')
plt.ylabel('Frequency')
plt.title('15 most frequent senders')
plt.show()     
        
raw_text = data['RawText'] #isolating the rawtext column
#print(raw_text[1]) #printing one cell from the rawtext column

from wordcloud import WordCloud, STOPWORDS
raw_list=[]
raw_text = data['RawText']
temp = [] #creating an empty temporary list
for i in raw_text: #a loop which eliminated 0's which occur from empty cells
    i = str(i) #interprettng each cell as a string
    i = i.strip().split()
    for x in i:
        temp.append(x)
raw_list = temp
temp_list = []

#this line removes punctuation
raw_list = [''.join(c for c in s if c not in string.punctuation) for s in raw_list]

stop = open('stopwords_en.txt', 'r')
stops = [] #initializing and cleaning the list of stopwords
stop_list = stop.readlines()
for i in stop_list:
    stops.append(i[:-1])
stop_list = stops

for i in raw_list: #This loops eliminates stop words from the data
    for x in i.split():
        if x not in stops:
            temp_list.append(x)
raw_list = temp_list
temp_list = [] 

for i in raw_list:
    if i.isdigit() == False:
        temp_list.append(i)
raw_list = temp_list #our cleaned list fo words

# Transforming the list into a string for displaying
text_str = ' '.join(raw_list)

# Crating and updating the stopword list
stpwords = set(STOPWORDS)
stpwords.add('will')
stpwords.add('said')


# Defining the wordcloud parameters
wc = WordCloud(background_color="white", max_words=2000, width=1000, height=1000,
               stopwords=stpwords)

# Generate word cloud
wc.generate(text_str)

# Store to file
wc.to_file('hillaryemailwordcloud.png')


print('\nThis is the wordcloud for the content of Hillarys emails')
# Show the cloud
plt.imshow(wc)
plt.axis('off')
plt.show()

print('done')