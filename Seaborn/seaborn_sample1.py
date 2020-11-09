#Author - xxxx
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

vidDF = pd.read_csv('vgsales.csv')
print "Dataset description: "
print '\n',vidDF.info() #dataframe details

#top genres
genres = Counter(vidDF['Genre'].dropna().tolist()).most_common(8) #to count the top 8 genres
#name of genre
genName = [name[0] for name in genres] 
#count of genre
genCount = [name[1] for name in genres]

fig1, ax1 = plt.subplots(figsize=(10,8))
sns.barplot(x=genName,y=genCount,ax=ax1)
plt.title('Genre Numbers',fontsize=20)
plt.ylabel("Number of Games",fontsize=15)
plt.xlabel("Genre",fontsize=15)

#top platforms
#to count the top 8 platforms
platforms = Counter(vidDF['Platform'].dropna().tolist()).most_common(8)
#platform name
platName = [name[0] for name in platforms]
#platform count
platCount = [name[1] for name in platforms]

fig2, ax2 = plt.subplots(figsize=(10,8))
sns.barplot(x=platName,y=platCount,ax=ax2,palette=sns.color_palette("pastel"))
plt.title('Platform Numbers',fontsize=20)
plt.ylabel("Number of Games",fontsize=15)
plt.xlabel("Platform",fontsize=15)

plt.show()