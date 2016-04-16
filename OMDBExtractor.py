import urllib2
import os
import csv
import time
import json
import re

with open('InputMovieList.csv', 'rb') as csvfile:

    spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
    mylist = []
    x = 0
    for row in spamreader:

        loopStartTime = time.time()
        movieID = row[0]
        try:
            req = urllib2.Request('http://www.omdbapi.com/?i=' + movieID, headers={
                'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'})
            html = urllib2.urlopen(req).read()
            data = json.loads(html,'utf-8')
            #data = ",".join(data).encode('utf-8')
            #print data
            #print(data)
            keys, values = zip(*data.items())
            if x==0:
               mylist.append("\t".join(keys).strip('"').encode('utf-8'))

            mylist.append("\t".join(values).encode('utf-8'))
            x += 1


        except:
            break

with open('omdbdata' + '.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter='\n')
    spamwriter.writerow(mylist)
print(mylist)