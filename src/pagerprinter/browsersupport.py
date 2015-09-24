#!/usr/bin/env python
"""
Browser backend support code.
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

from subprocess import Popen
from time import sleep


class BrowserBackend(object):
	def __init__(self, browser_executable, browser_delay):
		self.browser_executable = browser_executable
		self.browser_delay = browser_delay


class Firefox(BrowserBackend):
	"""\
Print backend support for Firefox / Iceweasel, requires extension
http://sites.google.com/site/torisugari/commandlineprint2
"""
	def print_url(self, url, printer=None, print_copies=1):
		for x in range(print_copies):
			if printer is None:
				Popen((
					self.browser_executable,
					'-print', url,
					'-printdelay', str(self.browser_delay)
				))
			else:
				Popen((
					self.browser_executable,
					'-print', url,
					'-printprinter', printer,
					'-printdelay', str(self.browser_delay)
				))
			if print_copies != 1:
				sleep(2)


class TestBrowser(BrowserBackend):
	def print_url(self, url, printer=None, print_copies=1):
		if printer is None:
			print "printing on default printer: %s" % url
		else:
			print "printing on specific printer (%s): %s" % (printer, url)

BROWSER_MAP = {
	'firefox': Firefox,
	'iceweasel': Firefox,
	'test': TestBrowser,
	'testbrowser': TestBrowser,
}


def get_browser(name):
	name = name.lower().strip()
	return BROWSER_MAP[name]
