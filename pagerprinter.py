#!/usr/bin/env python
"""
Program to automatically print out CFS pager feeds.
Copyright 2011 Michael Farrell <http://micolous.id.au/>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from pagerscraper import get_scraper
from browsersupport import get_browser
from mappingsupport import get_map
from ConfigParser import ConfigParser
from sys import argv

def main(fn):
	print """\
pagerprinter v0.1
Copyright 2011 Michael Farrell <http://micolous.id.au/>
"""
	# parse config
	c = ConfigParser()
	c.readfp(open(fn, 'rb'))
	
	# get a scraper instance
	scraper = get_scraper(c.get('pagerprinter', 'backend'))
	
	# get a browser helper instance
	browser = get_browser(c.get('pagerprinter', 'browser'))(c.get('pagerprinter', 'browser-exec'))
	
	trigger = c.get('pagerprinter', 'trigger').lower().strip()
	trigger_end = c.get('pagerprinter', 'trigger-end').lower().strip()
	my_unit = c.get('pagerprinter', 'unit').lower().strip()
	
	printer = None
	if c.has_option('pagerprinter', 'printer'):
		printer = c.get('pagerprinter', 'printer')
	
	mapper = 'google'
	if c.has_option('pagerprinter', 'mapper'):
		mapper = c.get('pagerprinter', 'mapper')
	
	mapper = get_map(mapper)
	
	# special case: all units.
	# may result in dupe printouts
	if my_unit == 'all':
		my_unit = ''
	
	# home
	home = c.get('pagerprinter', 'home')
	
	# now, lets setup a handler for these events.
	def page_handler(good_parse, msg, date=None, unit=None):
		if good_parse:
			print "Good parse! %s - %s" % (repr(msg), unit)
			# filter for unit
			if my_unit in unit.lower():
				# this is for me!!!
				print "- This is a message for my unit!"
				# check for trigger
				lmsg = msg.lower()
				if trigger in lmsg:
					# trigger found
					# split by trigger and find address nicely.
					addr = lmsg.split(trigger)[1]
					
					if trigger_end in lmsg:
						addr = addr.split(trigger_end)[0]
						
						# now split that up into parts, discarding the first which is a description of the event
						addr = ','.join(addr.split(',')[1:])
						
						# we have an address.  feed it to the mapping engine
						url = mapper.get_url(home, addr)
						
						print "- Address: %s" % addr
						print "- URL for directions: %s" % url
						
						# sending to browser
						browser.print_url(url, printer)
					else:
						print "- WARNING: End trigger not found!  Skipping..."
					
				else:
					print "- Trigger not found.  Skipping..."
			else:
				print "- This isn't for my unit.  Skipping..."
		else:
			print "ERROR: THIS IS A BUG!!!"
			print "Couldn't handle the following message, please file a bug report."
			print repr(msg)
	
	print "updating forever"
	scraper.update_forever(page_handler)
	

if __name__ == '__main__':
	configfile = 'pagerprinter.ini'
	
	if len(argv) >= 2:
		configfile = argv[1]
	main(configfile)
