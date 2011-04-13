#!/usr/bin/env python
"""
Browser backend support code.
"""

from subprocess import Popen


class Firefox(object):
	"""Print backend support for Firefox / Iceweasel, requires extension http://sites.google.com/site/torisugari/commandlineprint2"""
	def __init__(self, browser_executable):
		self.browser_executable = browser_executable
	
	def print_url(self, url, printer=None):
		if printer == None:
			Popen((self.browser_executable, '-print', url))
			
		else:
			Popen((self.browser_executable, '-print', url, '-printprinter', printer))

BROWSER_MAP = {
	'firefox': Firefox,
	'iceweasel': Firefox,
}

def get_browser(name):
	name = name.lower().strip()
	return BROWSER_MAP[name]


