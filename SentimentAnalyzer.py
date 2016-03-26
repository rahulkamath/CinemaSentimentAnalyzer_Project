from textblob import TextBlob
import csv
import time
import os
from collections import OrderedDict
import pandas as pd
startTime = time.time()
rootdir = 'RottenTomatoesData/'


for subdir, dirs, files in os.walk(rootdir):
    resultSet = []
    for file in files:

        with open(rootdir+file, 'rb') as csvfile:
            commentSentimentCount = OrderedDict([("name",""),("positive",0), ("negative", 0), ("neutral", 0)])
            spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
            commentSentimentCount['name']=file.replace(".csv","")
            for row in spamreader:
                blob = TextBlob(row[0].decode('utf-8'))
                if blob.sentiment.polarity>=0.1:
                    commentSentimentCount['positive'] += 1
                elif blob.sentiment.polarity<0:
                    commentSentimentCount['negative'] += 1
                else:
                    commentSentimentCount['neutral'] +=1
            keys, values = zip(*commentSentimentCount.items())
            #print ','.join(keys)
            resultSet.append(','.join([str(i) for i in values]))

        #print(commentSentimentCount)
    df = pd.DataFrame(resultSet)
    df.to_csv('sentimentAnalysis.csv')


print("Time taken is %s seconds" % (time.time()-startTime))

