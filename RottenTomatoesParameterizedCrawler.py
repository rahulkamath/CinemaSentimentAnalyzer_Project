import urllib2
from bs4 import BeautifulSoup
import csv
import time
import sys

startTime = time.time()

mylist = []
loopStartTime = time.time()

movieString = sys.argv[1]
pageNumber = ""
x = 0
while True:

    try:
        req = urllib2.Request(
            'http://www.rottentomatoes.com/m/' + movieString + '/reviews/?' + pageNumber + '&type=user&sort=',
            headers={'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'})
        html = urllib2.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        count = soup.findAll("div", class_="user_review").__len__()
        if count == 0:
            break
        for i in range(0, count):
            mylist.append(soup.findAll("div", class_="user_review")[i].contents[2].encode('utf-8').strip())
        pageNumber = "page=%d" % x
        x = x + 1

    except:
        break

print mylist.__len__()
print("Time taken is %s seconds" % (time.time() - loopStartTime))
with open(movieString + '.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter='\n')
    spamwriter.writerow(mylist)

print("Total Time taken is %s seconds" % (time.time()-startTime))
