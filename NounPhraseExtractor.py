import os
from textblob import TextBlob
import csv
import time
startTime = time.time()
#rootdir = 'RottenTomatoesData/'
rootdir = 'IMDbCrawlerData/'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        loopStartTime = time.time()
        movieString = os.path.join(subdir, file)
        #filename = movieString.replace(".csv","_np.csv").replace("RottenTomatoesData","RottenTomatoesNPData")
        filename = movieString.replace(".csv","_np.csv").replace("IMDbCrawlerData","IMDbCrawlerNPData")
        print filename
        with open(movieString, 'rb') as csvfile:
            nounPhrases = []
            spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
            for row in spamreader:
                blob = TextBlob(row[0].decode('utf-8'))
                wordList = blob.noun_phrases
                nounPhrases.append(','.join(wordList).encode('utf-8'))
            print("Time taken is %s seconds" % (time.time()-loopStartTime))
            with open(filename, 'wb') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter='\n')
                spamwriter.writerow(nounPhrases)
print("Total Time taken is %s seconds" % (time.time()-startTime))