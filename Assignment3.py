import argparse
import sys
import csv
import urllib2
import re
from operator import itemgetter

parser = argparse.ArgumentParser()
parser.add_argument("--url")
args = parser.parse_args()
url = args.url
	
data = urllib2.urlopen(url)

csvdata = csv.reader(data)

totalhits = 0.0
imagehits = 0.0
otherhits = 0.0	
firefoxhits = 0.0
chromehits = 0.0
IEhits = 0.0
safarihits = 0.0
otherbrowserhits = 0.0	
for row in csvdata:
	totalhits += 1
	imgmatch = re.search('.*(\.jpg|\.png|\.gif)',row[0])
	if imgmatch is None:
		otherhits += 1
	else:
		imagehits += 1
	
	browsermatch = re.search('([Ff]irefox)|([Cc]hrome)|(MSIE)|([Ss]afari)',row[2])
	if browsermatch is not None:
		if(browsermatch.group(1)) is not None:
			firefoxhits += 1
		elif(browsermatch.group(2)) is not None:
			chromehits += 1
		elif(browsermatch.group(3)) is not None:
			IEhits += 1
		elif(browsermatch.group(4)) is not None:
			safarihits += 1
		else:
			otherbrowserhits += 1
list = [("Firefox",firefoxhits),("Chrome",chromehits),("Internet Explorer",IEhits),("Safari",safarihits),("Other",otherbrowserhits)]

topbrowser = sorted(list,key=itemgetter(1), reverse = 1)[0][0]


print "Images account for  %2.2f%% of total hits" % (imagehits/totalhits*100)
print "The most popular browser for this website was: %s" % topbrowser

