#!/bin/python
# https://dev.to/rhymes/how-to-make-python-code-concurrent-with-3-lines-of-code-2fpe

import requests
# to supress https InsecureRequestWarning (part of requests)
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from datetime import datetime
# concurrency
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

def urlfetch(url):
	return requests.get(url, verify=False)

f = open('security_news_url.lst', 'ro')
urlL = []

for u in f.readlines():
	urlL.append(u.rstrip())

#urlL = urlL*(500/len(urlL))
#r = requests.get(urlL[0])
#print r.status_code

# No Concurrency
starttime = datetime.now()
for url in urlL:
	urlfetch(url)
finishtime = datetime.now()

print "Seconds for requesting "+str(len(urlL))+" URLs without concurrency:" 
print str((finishtime - starttime).total_seconds())

# Thread Concurrency
starttime = datetime.now()
with ThreadPoolExecutor(max_workers=4) as executor:
	for _ in executor.map(urlfetch, urlL):
		pass
finishtime = datetime.now()

print "Seconds for requesting "+str(len(urlL))+" URLs with concurrency (thread):" 
print str((finishtime - starttime).total_seconds())

# Process Concurrency
starttime = datetime.now()
with ProcessPoolExecutor(max_workers=4) as executor:
	for _ in executor.map(urlfetch, urlL):
		pass
finishtime = datetime.now()

print "Seconds for requesting "+str(len(urlL))+" URLs with concurrency (process):" 
print str((finishtime - starttime).total_seconds())



