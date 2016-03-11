import urllib2
from bs4 import BeautifulSoup
import csv
import time
import re

startTime = time.time()

with open('movieListIMDB.csv', 'rb') as csvfile:
    mylist = []
    spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
    for row in spamreader:
        movieString = row[0]
        pageNumber = ""
        x=0
        while True:

            try:
                req = urllib2.Request('http://www.imdb.com/title/'+movieString+'/reviews?'+pageNumber, headers={ 'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11' })
                html = urllib2.urlopen(req).read()
                soup = BeautifulSoup(html, 'html.parser').get_text()


                prelim = re.findall('found the following review useful:(.*?)Was the above review', soup, re.DOTALL|re.MULTILINE)
                splitByNewline = ''.join(prelim)
                commentArr = splitByNewline.split('\n\n\n')
                for i in range(0,commentArr.__len__()):
                    if i%3!=0:
                        mylist.append(commentArr[i].encode('utf-8').strip())

                count = prelim.__len__()
                print(count)
                if count<=0:
                    break

                pageNumber = "start=%d" % x
                x = x+10

            except:
                break


        print mylist.__len__()

        with open(movieString+'.csv', 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter='\n')
            spamwriter.writerow(mylist)

print("Time taken is %s seconds" % (time.time()-startTime))
