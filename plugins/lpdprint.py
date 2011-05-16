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

from plugins import BasePlugin
from subprocess import Popen, PIPE


class LPDPrintPlugin(BasePlugin):
	"""\
This plugin prints out a text document using LPD/CUPS of the details, using the
lpr command.
"""
	def execute(self, msg, unit, address, when, printer, print_copies):
		if printer != None:
			lpr = Popen(('lpr', '-#', str(print_copies), '-P', printer), stdin=PIPE)
		else:
			lpr = Popen(('lpr', '-#', str(print_copies)), stdin=PIPE)

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
