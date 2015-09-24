#!/usr/bin/env python
"""
Email plugin
Copyright 2013 Shane Rees <https://github.com/Shaggs/>

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
from . import BasePlugin
import smtplib
from email.mime.text import MIMEText


class EmailPlugin(BasePlugin):
	def configure(self, c):
		# read in phone numbers we need
		self.recipient = [
			x.strip()
			for x
			in c.get('email', 'to').lower().split(',')
		]

		self.hostname = c.get('email', 'hostname')
		self.username = c.get('email', 'username')
		self.password = c.get('email', 'password')
		self.fromaddr = c.get('email', 'from')

	def execute(self, msg, unit, address, when, printer, print_copies):
		msg = MIMEText('%s - %s' % (msg, unit))

		for recipient in self.recipient:
			server = smtplib.SMTP(self.hostname)
			server.ehlo()
			server.starttls()
			msg['Subject'] = "FIRE CALL: %s - %s" % (msg, unit)
			msg['From'] = self.fromaddr
			msg['To'] = recipient
			server.login(self.username, self.password)
			server.sendmail(self.fromaddr, recipient, msg.as_string())
			server.quit()

PLUGIN = EmailPlugin
