import urllib2
from bs4 import BeautifulSoup
import csv
import time
import re

startTime = time.time()

with open('test.csv', 'rb') as csvfile:
    mylist = []
    spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
    for row in spamreader:
        movieString = row[0]
        pageNumber = "start=0"
        x = 0
        continueFlag = True
        while continueFlag:
            try:
                req = urllib2.Request('http://www.imdb.com/title/'+movieString+'/reviews?'+pageNumber, headers={ 'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11' })
                html = urllib2.urlopen(req).read()
                soup = BeautifulSoup(html, 'html.parser')
                count = soup.findAll("div",   id="tn15content").__len__()
                if count == 0:
                    break
                for i in range(0,count):
                    fullStr = soup.findAll("div",  id="tn15content")[i].contents[11].encode('utf-8').strip()
                    fullStr = fullStr.replace('<b>*** This review may contain spoilers ***</b>', ' ')
                    fullStr = fullStr.replace('Add another review', ' ')
                    fullStr = fullStr.replace('"', ' ')
                    fullStr = fullStr.replace('\n', ' ').replace('\r', '')
                    commArr = re.findall('<p>(.*?)</p>',fullStr)
                    if commArr.__len__() == 1:
                        continueFlag = False
                    print 'Length'
                    print commArr.__len__()
                    for eachStr in commArr:
                        cleanR = re.compile('<.*?>')
                        cleanText = re.sub(cleanR,'', eachStr)
                        mylist.append(cleanText)
                x += 1
                pageNumber = "start=%d" % (x*10)
            except:
                break
        print mylist.__len__()
        with open(movieString+'.csv', 'wb') as csvFile:
            spamWriter = csv.writer(csvFile, delimiter='\n')
            spamWriter.writerow(mylist)

print("Time taken is %s seconds" % (time.time()-startTime))