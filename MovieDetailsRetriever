import urllib2
import os
from textblob import TextBlob
import csv
import time
import json
import re
startTime = time.time()
#rootdir = 'RottenTomatoesData/'
rootdir = 'IMDbCrawlerNPData/'

def replace_all(text, dic):
    for i, j in dic.iteritems():
        arr = j.split(",")
        for word in arr:
            text = re.sub(r"\b%s\b" % re.escape(word.lower().strip()),i,text)
        #text = text.replace(j.lower(), i)
    return text.encode('utf-8')

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        loopStartTime = time.time()
        movieString = os.path.join(subdir, file)
        filename = movieString.replace(".csv","_clean.csv").replace("IMDbCrawlerNPData","IMDbCrawlerNPDataClean")
        movieID = movieString.replace("_np.csv","").replace("IMDbCrawlerNPData/","")
        req = urllib2.Request('http://www.omdbapi.com/?i='+movieID,headers={'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'})
        html = urllib2.urlopen(req).read()
        data = json.loads(html)
        with open(movieString, 'rb') as csvfile:
            replacedData = []
            spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
            for row in spamreader:
                if len(row)!=0:
                    replacedData.append(replace_all(row[0].decode('utf-8'),data))

            with open(filename, 'wb') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter='\n')
                spamwriter.writerow(replacedData)



print("Total Time taken is %s seconds" % (time.time()-startTime))