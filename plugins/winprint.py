#!/usr/bin/env python
"""
Windows text printing plugin for pagerprinter.
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
from traceback import print_exc
try:
	from win32api import ShellExecute
except ImportError, ex:
	print_exc()
	print "NOTICE: winprint could not be loaded on this platform."
	PLUGIN = None
else:
	from tempfile import mktemp

	class WinPrintPlugin(BasePlugin):
		"""This plugin prints out a text document on Windows of the details."""
		def execute(self, msg, unit, address, when, printer, print_copies):
			filename = mktemp('.txt')

			open(filename, 'w').write("""\
Got a page!

Unit: %(unit)s
Address: %(address)s
When: %(when)s

%(msg)s
""" % dict(msg=msg, unit=unit, address=address, when=when.ctime()))

			if printer == None:
				action = 'print'
			else:
				action = 'printto'
				printer = '"%s"' % printer
		
			for x in range(print_copies):
				ShellExecute(
					0,
					action,
					filename,
					printer,
					'.',
					0
				)

	PLUGIN = WinPrintPlugin
