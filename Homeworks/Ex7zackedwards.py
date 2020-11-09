#Author Zack Edwards

import re
import nltk
import pandas as pd
import string

#entering files
pro_file = open('ProGuns.txt', 'r+')
pro = pro_file.readlines()
pro_temp = []
against_file = open('AgainstGuns.txt', 'r+')
against = against_file.readlines()
against_temp = []
stop = open('stopwords_en.txt', 'r')

#cleaning the data for the pro position
for i in pro: #This loop gets rid of unwanted lines and notations like \n
    i = i.strip()
    if 'ReplyReplies' in i:
        continue
    elif 'Reply' in i:
        continue
    elif '+' in i:
        continue
    elif len(i.split()) >= 3:
        pro_temp.append(i)
        
pro = pro_temp
pro_temp = []

for i in pro: #This loops gets ride of the punctuation
    l = nltk.word_tokenize(i)
    ll = [x for x in l if not re.fullmatch('[' + string.punctuation + ']+', x)]
    ll = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in ll]).strip()
    pro_temp.append(str(ll))
pro = pro_temp

stops = [] #initializing and cleaning the list of stopwords
stop_list = stop.readlines()
for i in stop_list:
    stops.append(i[:-1])
stop_list = stops

pro_temp = []

for i in pro: #This loops eliminates stop words from the data
    for x in i.split():
        if x not in stops:
            pro_temp.append(x)
pro = pro_temp #This is our final list of words for the pro argument
print('The following is the first 20 clean data points from the pro argument')
print(pro[:20])

#cleaning up the data from the against argument

for i in against: #The steps are the same for cleaning pro and against
    i = i.strip()
    if 'ReplyReplies' in i:
        continue
    elif 'Reply' in i:
        continue
    elif '+' in i:
        continue
    elif len(i.split()) >= 3:
        against_temp.append(i)
        
against = against_temp
against_temp = []

for i in against:
    l = nltk.word_tokenize(i)
    ll = [x for x in l if not re.fullmatch('[' + string.punctuation + ']+', x)]
    ll = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in ll]).strip()
    against_temp.append(str(ll))
against = against_temp

against_temp = []

for i in against:
    for x in i.split():
        if x not in stop_list:
            against_temp.append(x)
against = against_temp
against_temp = []
print('The following is the first 20 clean data points from the against argument')
print(against[:20]) #This is the final list of words for the against argument


# importing the library
from nltk.corpus import sentiwordnet as swn
pro_tags = nltk.pos_tag(pro)
against_tags = nltk.pos_tag(against)
Pos_pos_total = 0
Pos_neg_total = 0

Con_pos_total = 0
Con_neg_total = 0

# looping into the list of words and printing the sentiment
for word in pro_tags:
    synsets = None
    if word[1] == ("JJ"):
        try:
            swn.senti_synset(word[0] + '.a.01').pos_score()
        except:
            continue
        Pos_pos_total += swn.senti_synset(word[0] + '.a.01').pos_score()
        Pos_neg_total += swn.senti_synset(word[0] + '.a.01').neg_score()

for word in against_tags:
    #print '\nword', word
    if word[1] == 'JJ':
        try:
            swn.senti_synset(word[0] + '.a.01').pos_score()
        except:
            continue
        Con_pos_total += swn.senti_synset(word[0] + '.a.01').pos_score()
        Con_neg_total += swn.senti_synset(word[0] + '.a.01').neg_score()

print( '\nthe positive score on the Positive article is', Pos_pos_total)
print ('\nthe negative score on the Positive article is', Pos_neg_total)
print('\nThe net score on the Positive article is ', Pos_pos_total - Pos_neg_total)
print( '\nthe positive score on the Against article is', Con_pos_total)
print ('\nthe negative score on the Against article is', Con_neg_total)
print('\nThe net score on the Against article is ', Con_pos_total - Con_neg_total)


# This script reads a text file, clean it in part and generates a word cloud
#   using the words in the text

# Importing the required libraries
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


# Save a lower-case version of each word to a list
words_list = []
for i in pro: 
	words_list.append(i.lower())

# Eliminate non alpha elements
text_list = [word.lower() for word in words_list if word.isalpha()]

# Transforming the list into a string for displaying
text_str = ' '.join(text_list)

# Crating and updating the stopword list
stpwords = set(STOPWORDS)
stpwords.add('will')
stpwords.add('said')

# Defining the wordcloud parameters
wc = WordCloud(background_color="white", max_words=2000,
               stopwords=stpwords)

# Generate word cloud
wc.generate(text_str)

# Store to file
wc.to_file('progun.png', '')


print('This is the wordcloud for the pro gun argument')
# Show the cloud
plt.imshow(wc)
plt.axis('off')
plt.show()

# Save a lower-case version of each word to a list
words_list = []
for i in against: 
	words_list.append(i.lower())

# Eliminate non alpha elements
text_list = [word.lower() for word in words_list if word.isalpha()]

# Transforming the list into a string for displaying
text_str = ' '.join(text_list)

# Crating and updating the stopword list
stpwords = set(STOPWORDS)
stpwords.add('will')
stpwords.add('said')

# Defining the wordcloud parameters
wc = WordCloud(background_color="white", max_words=2000,
               stopwords=stpwords)

# Generate word cloud
wc.generate(text_str)

# Store to file
wc.to_file('againstgun.png')

print('This is the word cloud for the against argument')
# Show the cloud
plt.imshow(wc)
plt.axis('off')
plt.show()
