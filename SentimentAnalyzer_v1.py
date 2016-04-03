from textblob import TextBlob
import csv
import time
import os
from collections import OrderedDict
import pandas as pd
import operator
startTime = time.time()
rootdir = 'RottenTomatoesData/'

def findMax(dic):
    highestCount = 0
    highestKey = ""
    for i,j in dic.iteritems():
        if j>highestCount and i!="name":
            highestCount=j
            highestKey = i

    return highestKey

for subdir, dirs, files in os.walk(rootdir):
    resultSet = ["Name,Great,Good,Average,Poor,Awful"]
    for file in files:

        with open(rootdir+file, 'rb') as csvfile:
            commentSentimentCount = OrderedDict([("name",""),("great",0),("good",0), ("average", 0),("poor",0), ("awful", 0)])
            spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
            commentSentimentCount['name']=file.replace(".csv","")
            for row in spamreader:
                blob = TextBlob(row[0].decode('utf-8'))
                sentimentScore = blob.sentiment.polarity
                if sentimentScore>=0.6:
                    commentSentimentCount['great'] += 1
                elif sentimentScore<0.6 and sentimentScore>=0.2:
                    commentSentimentCount['good'] += 1
                elif sentimentScore<0.2 and sentimentScore>=-0.2:
                    commentSentimentCount['average'] += 1
                elif sentimentScore <-0.2 and sentimentScore >= -0.6:
                    commentSentimentCount['poor'] += 1
                else:
                    commentSentimentCount['awful'] +=1

            maxKey = findMax(commentSentimentCount)

            for i in commentSentimentCount:
                if i!="name":
                    commentSentimentCount[i]="No"
            commentSentimentCount[maxKey] = "Yes"

            #print ','.join(keys)
            keys, values = zip(*commentSentimentCount.items())

            resultSet.append(",".join([str(i) for i in values]))

        #print(commentSentimentCount)

    df = pd.DataFrame(resultSet)
    df.to_csv('sentimentAnalysis_v1.csv')


print("Time taken is %s seconds" % (time.time()-startTime))

