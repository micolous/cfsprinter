#!/usr/bin/env python
"""
Scraper for PDW / SACFS
Copyright 2010 - 2015 Michael Farrell <http://micolous.id.au/>

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

from __future__ import absolute_import
import asyncore
from datetime import datetime
from smtpd import SMTPServer
from email import message_from_string
from .sacfs_flexcode import CODES


__all__ = [
	'CFSPDWScraper',
]


class PDWServer(SMTPServer):
	def __init__(self, localaddr, handler):
		SMTPServer.__init__(self, localaddr, None)
		self.handler = handler

	def process_message(self, peer, mailfrom, rcpttos, data):
		# parse the message
		mime_message = message_from_string(data)
		message = mime_message.get_payload()

		flexcode, mtime, mdate, msg = message.split(' ', 3)

		when = datetime.strptime(mdate + 'T' + mtime, '%d-%m-%yT%H:%M:%S')
		flexcode = int(flexcode)
		msg = msg.strip()

		if flexcode not in CODES:
			print 'flexcode %d is not known' % flexcode
			print 'page:', flexcode, when, msg
			return
		else:
			print 'page: %s (%s) %s %s' % (flexcode, CODES[flexcode], when, msg)

			self.handler(
				good_parse=True,
				date=when,
				unit=CODES[flexcode],
				msg=msg
			)


class CFSPDWScraper(object):
	"""
	This uses the PDW application on Windows (also works in WINE) to decode
	pages in FLEX format.

	This module runs an SMTP server on ``localhost:8825`` which you should
	configure PDW to send messages at.

	This server ignores authentication and the source and destination email
	addresses.

	Configure PDW to output with **only** these fields, in the message body:
	- Address
	- Time
	- Date
	- Message

	Do not add any other fields into the email otherwise it will not parse.

	This code does not presently handle multipart / fragmented pages.
	"""
	def __init__(self, update_frequency=None):
		# Update frequency is not relevant
		self.feed_handler = None
		self._smtp = PDWServer(('localhost', 8825), self.handler)

	def handler(self, **kwargs):
		self.feed_handler(**kwargs)

	def update(self, feed_handler):
		"""
		Pings feed for new events.
		"""
		self.feed_handler = feed_handler

	def update_forever(self, feed_handler):
		self.update(feed_handler)
		asyncore.loop()
