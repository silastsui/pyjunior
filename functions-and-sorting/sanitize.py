#!/usr/bin/python
#replace crap with poo

def sanitize(sen,bad,good):
	newsen = sen.replace(bad,good)
	return newsen

x = "oh crap, I crapped in the crappy crapper" * 10000000
sanitize(x,"crap","poo")
