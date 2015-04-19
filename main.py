# -*- coding: utf-8 -*-

import time
import urllib2
from urllib2 import urlopen
import re
import cookielib, urllib2
from cookielib import CookieJar
import datetime
import os
    

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# webUrl = 'http://ticket.7net.com.tw/index.php?class=order&func=allgenki&game_id=86955&category=ibon'
webUrl = 'http://ticket.7net.com.tw/index.php?class=order&func=allgenki&game_id=82284&category=ibon'
soldOut = u'已售完'
pleaseChoice = u'請選擇'

def playsound(frequency,duration):
   	#apt-get install beep
    os.system('beep -f %s -l %s' % (frequency,duration))
    os.system('/usr/bin/printf "\a"')

def parsingIbonData():
	isSoldOut = True
	ticketSections = []
	sourceCode = opener.open(webUrl).read()
	try:
		salesStatus = re.findall(r'<option value=\'.*\'>(.*?)</option>', sourceCode)
		for status in salesStatus:
			utf8Status = status.decode('utf8')
			if pleaseChoice in utf8Status:
				continue

			# print utf8Status
			if soldOut not in utf8Status:
				isSoldOut = False;
				ticketSections.append(utf8Status)

   		if not isSoldOut:
   			playsound(2500, 1000)
   			playsound(2500, 1000)
   			
   			print datetime.datetime.now().strftime(" ===== %Y-%m-%d %H:%M:%S ===== ")   			
   			for section in ticketSections:
   				print section

	except Exception, e:
		print str(e)

def main():
    try:
    	while True:
			parsingIbonData()
			time.sleep(1)
    except Exception,e:
        print str(e)
        pass

    while True:
    	try:
			parsingIbonData()
    	except Exception,e:
        	print str(e)
       	
		time.sleep(1)

		

main()