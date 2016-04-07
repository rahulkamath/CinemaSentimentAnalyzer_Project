import urllib2
from bs4 import BeautifulSoup
import csv
import time
import re

startTime = time.time()
with open('movieListIMDB.csv', 'rb') as csvFile:
    spamReader = csv.reader(csvFile, delimiter='\n', quotechar='|')
    myList = []
    loopStartTime = time.time()
    for row in spamReader:
        myArr = []
        movieString = row[0]
        try:
            req = urllib2.Request('http://www.imdb.com/title/'+movieString,
                                  headers={'User-Agent': 'Mozilla/5.0 (X11; U; '
                                                         'Linux i686) Gecko/20071127 Firefox/2.0.0.11'})
            html = urllib2.urlopen(req).read()
            soup = BeautifulSoup(html, 'html.parser')
            myElement = soup.findAll("div", class_="rec_item")
            myElementStr = str(myElement).encode('utf-8').strip()
            myArr = re.findall('data-tconst=\"(.*?)\"', myElementStr)
            #myElement = soup.findAll(attrs={"name" : "data-tconst"})
            count = myArr.__len__()
            if count == 0:
                break
        except:
            break
        myList.extend(myArr)

    print("Time taken is %s seconds" % (time.time()-loopStartTime))
    with open('RecommendedMovieList.csv', 'wb') as csvFile2:
        spamWriter = csv.writer(csvFile2, delimiter='\n')
        spamWriter.writerow(myList)

print("Total Time taken is %s seconds" % (time.time()-startTime))