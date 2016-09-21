#!/usr/bin/python
#sanitize.py

def sanitize(sen,bad,good):
	bad_len = len(bad)
	for x in xrange(len(sen)):
		if sen[x:x+bad_len] == bad:
			sen = sen[:x] + good + sen[x+bad_len:]
	return sen	

x = "oh crap, I crapped in the crappy crapper" * 15000
sanitize(x,"crap","poop")
