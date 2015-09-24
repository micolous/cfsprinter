#!/usr/bin/env python
"""
Log file plugin for pagerprinter.
Copyright 2011 - 2015 Michael Farrell <http://micolous.id.au/>

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


class LogFilePlugin(BasePlugin):
	"""This plugin prints out a text document on Windows of the details."""

	def configure(self, c):
		# open the log file.
		self.logfile = c.get('logfile', 'filename')

		self.linefeed = (c.getboolean('logfile', 'crlf') and '\r\n') or '\n'

	def execute(self, msg, unit, address, when, printer, print_copies):
		with open(self.logfile, 'ab') as fh:
			fh.write("%(when)s - %(unit)s - %(msg)s%(lf)s" % dict(
				when=when.ctime(), unit=unit, msg=msg, lf=self.linefeed)
			)

PLUGIN = LogFilePlugin

