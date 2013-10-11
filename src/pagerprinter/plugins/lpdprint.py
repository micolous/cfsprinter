#!/usr/bin/env python
"""
LPD/CUPS text printing plugin for pagerprinter.
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
from __future__ import absolute_import
from . import BasePlugin
from subprocess import Popen, PIPE
from configparser import NoOptionError


class LPDPrintPlugin(BasePlugin):
	"""\
This plugin prints out a text document using LPD/CUPS of the details, using the
lpr command.
"""
	def configure(self, c):
		try:
			self.cpi = c.getint('pagerprinter', 'print-cpi')
		except NoOptionError:
			self.cpi = None
		
		try:
			self.lpi = c.getint('pagerprinter', 'print-lpi')
		except NoOptionError:
			self.lpi = None

	def execute(self, msg, unit, address, when, printer, print_copies):
		pargs = ['lpr', '-#', str(print_copies)]

		if printer != None:
			pargs += ['-P', printer]

		if self.cpi != None:
			pargs += ['-o', 'cpi=%d' % self.cpi]
		
		if self.lpi != None:
			pargs += ['-o', 'lpi=%d' % self.lpi]

		lpr = Popen(pargs, stdin=PIPE)

		lpr.stdin.write("""\
Got a page!

Unit: %(unit)s
Address: %(address)s
When: %(when)s

%(msg)s
""" % dict(msg=msg, unit=unit, address=address, when=when.ctime()))

		lpr.stdin.flush()
		lpr.stdin.close()

PLUGIN = LPDPrintPlugin
