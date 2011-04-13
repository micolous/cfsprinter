#!/usr/bin/env python
"""
Browser backend support code.
"""

from subprocess import Popen

class BrowserBackend(object):
	def __init__(self, browser_executable):
		self.browser_executable = browser_executable

class Firefox(BrowserBackend):
	"""Print backend support for Firefox / Iceweasel, requires extension http://sites.google.com/site/torisugari/commandlineprint2"""
	
	def print_url(self, url, printer=None):
		if printer == None:
			Popen((self.browser_executable, '-print', url, '-printdelay', '20'))
			
		else:
			Popen((self.browser_executable, '-print', url, '-printprinter', printer, '-printdelay', '20'))

class TestBrowser(BrowserBackend):
	def print_url(self, url, printer=None):
		if printer == None:
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

