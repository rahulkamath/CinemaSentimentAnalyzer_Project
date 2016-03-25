from textblob import TextBlob
import csv
import time

startTime = time.time()
movieString = "RottenTomatoesData/beowulf"

commentSentimentCount = {"positive":0,"negative":0,"neutral":0}

with open(movieString+'.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
    for row in spamreader:
        blob = TextBlob(row[0].decode('utf-8'))
        print(blob.noun_phrases)

        if blob.sentiment.polarity>=0.1:
            commentSentimentCount['positive'] += 1
        elif blob.sentiment.polarity<=-0.1:
            commentSentimentCount['negative'] += 1
        else:
            commentSentimentCount['neutral'] +=1
print(commentSentimentCount)
print("Time taken is %s seconds" % (time.time()-startTime))

