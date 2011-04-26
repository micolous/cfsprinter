#!/usr/bin/env python
"""
Library to scrape events from the CFS pager feed (South Australian Country Fire Service).
Copyright 2010 - 2011 Michael Farrell <http://micolous.id.au/>

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

import re
from time import sleep, time
from datetime import datetime
from urllib2 import urlopen
from datetime import datetime
from xml.sax.saxutils import unescape
try:
	# python >=2.6
	import json
except:
	# python <=2.5
	import simplejson as json


def strip_tags(value):
	"Return the given HTML with all tags stripped."
	return re.sub(r'<[^>]*?>', '', value)

class CFSPagerScraper(object):
	feed = 'http://paging.sacfs.org/feed1/live/ajax/update.php?f='
	last_update = int(time()) - 3600
	message_parser = re.compile(r'<td class="date">(?P<date>.+)</td>\s*<td class="message">\s*(?P<msg>.+)\sw*<span class="name">-\s*(?P<unit>.+)\s*</span></td></tr>')
	def __init__(self, update_frequency=30):
		self.update_frequency = int(update_frequency)
		
	def update(self, feed_handler):
		"""
Pings the feed for new events.  Uses a callback, feed_handler, which is called as follows:

The first parameter, good_parse, indicates whether the parser activated successfully for the whole message.  If this is true, you'll get the following parameters:

date: A datetime.datetime object representing the time of the event.  If the date couldn't be parsed, then a unicode string will be returned containing the raw information.
unit: The unit that this message is directed at.
msg: The full message.

If the good_parse is False, you'll get this instead:

msg: The full message from the server, minus HTML tags.

"""
		# download the new feed
		fp = urlopen(self.feed + str(self.last_update))
		data = json.load(fp)
		self.last_update = data['timestamp']
	
		messages_sent = 0
		if data['updated']:
	
			# feed was updated, start posting.
			messages = data['data'].split('<tr class="page">')
			for message in messages[1:]:
				#print message
				result = self.message_parser.match(message)
				
				# report back to the handler on what our status is.
				try:
					d = datetime.strptime(result.group('date'), '%d-%m-%y %H:%M:%S')
				except:
					d = result.group('date')
				if result == None:
					feed_handler(good_parse=False, msg=strip_tags(message))
				else:
					feed_handler(good_parse=True, date=d, unit=result.group('unit'), msg=unescape(result.group('msg')))

	def update_forever(self, feed_handler):
		"""\
Like update, except the feed is updated continuously forever.  Error handling is your job.
"""
		while True:
			self.update(feed_handler)
			print "napping..."
			sleep(self.update_frequency)

SCRAPER_MAP = {
	'sacfs': CFSPagerScraper
}

def get_scraper(name):
	name = name.lower().strip()
	
	return SCRAPER_MAP[name]

if __name__ == '__main__':
	def test_handler(good_parse, **message):
		print "msg = %s" % message
	
	print "Activating test program..."
	scraper = CFSPagerScraper()
	scraper.update_forever(test_handler)

