import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
import pandas as pd
import csv
import nltk
from collections import Counter #importing all nessecary libraries

stop = open('stopwords_en.txt', 'r')
stops = [] #initializing and cleaning the list of stopwords
stop_list = stop.readlines()
for i in stop_list:
    stops.append(i[:-1])
stop_list = stops
#print(stop_list)

tweets = open('hoboken_tweets.csv', 'r') #opening the tweets file and reading it in a data frame
df = pd.read_csv(tweets)
#df.head()

senders_list = list(df['screen_name']) #isolate the senders
top10 = Counter(senders_list).most_common(10) #calculate the top 10
print('\nThe 10 most frequest users and the amount of tweets they sent are: ', top10)

word_list = []
for index, row in df['text'].iteritems():
    text_str = str(row) #change to string
    tokens = nltk.word_tokenize(text_str) #tokenize/ isolate each word
    alphabet = [word for word in tokens if word.isalpha()] #remove non alphabetical words
    lowercase = [word.lower() for word in alphabet] #make all words uniform (lowercase)
    no_stopwords = []
    for i in lowercase:
        if i not in stop_list and len(i) > 2 and i != 'https': #remove stopwords and the urls
            no_stopwords.append(i)
    word_list.extend(no_stopwords)
    
top_50 = Counter(word_list).most_common(10) #calculate the top 10 used words
print('\nThese are the top 10 most used words and how many times they were used: ', top_50)

word = []
frequency = []

for i in range(len(top_50)):
    word.append(top_50[i][0])
    frequency.append(top_50[i][1])


plt.bar(word, frequency, color='r')
plt.title('Top 10 Words')
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.show()

user = []
amount = []

for i in range(len(top10)):
    user.append(top10[i][0])
    amount.append(top10[i][1])


plt.bar(user, amount, color='r')
plt.title('Top 10 users')
plt.xlabel('User')
plt.ylabel('Amount of tweets')
plt.show()


stop.close()
tweets.close()