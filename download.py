import urllib2
from bs4 import BeautifulSoup

url = "http://gointothestory.blcklst.com/free-script-downloads/"
html = urllib2.urlopen(url)
soup = BeautifulSoup(html)

imgs = soup.findAll("div", {"class":"poster_holder"})
for pdf in pdfs:
        print pdf.a['href'].split("imgurl=")[1]