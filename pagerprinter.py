#!/usr/bin/env python

from pagerscraper import get_scraper
from browsersupport import get_browser
from ConfigParser import ConfigParser
from sys import argv

def main(fn):
	# parse config
	c = ConfigParser()
	c.readfp(open(fn, 'rb'))
	
	# get a scraper instance
	scraper = get_scraper(c.get('pagerprinter', 'backend'))
	
	# get a browser helper instance
	browser = get_browser(c.get('pagerprinter', 'browser'))(c.get('pagerprinter', 'browser-exe'))
	
	
	

if __name__ == '__main__':
	configfile = 'pagerprinter.ini'
	
	if len(argv) >= 2:
		configfile = argv[1]
	main(configfile)
