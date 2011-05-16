#!/usr/bin/env python
"""
Skype SMS plugin for pagerprinter.
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


Skype documentation that isn't behind a wall, because Skype have some
funny ideas about the definition of "open source projects", that they
can demand you to sign up for a developer programme when you really
don't need to:
	<http://skype4py.sourceforge.net/doc/html/>

Library download:
	<http://sourceforge.net/projects/skype4py/files/>

Note that the API is entirely un-pythonic, so be careful.  It seems
like .NET coding conventions.

If you're finding yourself sending a lot of messages, sign up for a
proper SMS gateway.  It's cheaper and doesn't require Skype to be
running.

"""

from plugins import BasePlugin

try:
	from Skype4Py import Skype, smsMessageTypeOutgoing
except ImportError:
	print "NOTICE: skypesms plugin requires Skype4Py to be installed"
	print "http://sourceforge.net/projects/skype4py/"
	PLUGIN = None
else:
	# make our plugin!
	class SkypePlugin(BasePlugin):
		def __init__(self):
			print "Attempting to connect to Skype API.  If Python crashes, this"
			print "could mean that Skype isn't running at the moment."
			print ""
			print "(There's no way around this at present -- Skype's Python"
			print "libraries suck.  It also this seems to crash all the time"
			print "on OSX.)"
			# connect to skype
			self.skype = Skype()

			# skype4py is quite un-pythonic, with it's method names.
			self.skype.Attach()

			# by now skype4py would crash if skype isn't running.

		def configure(self, c):
			# read in phone numbers we need
			self.numbers = [
				x.strip()
				for x
				in c.get('skypesms', 'to').lower().split(',')
			]

		def execute(self, msg, unit, address, when, printer, print_copies):
			# lets just send the whole message verbatim.
			sms = self.skype.CreateSms(smsMessageTypeOutgoing, *self.numbers)
			sms.Body = "%s: %s - %s" % (when.ctime(), msg, unit)
			sms.Send()

	PLUGIN = SkypePlugin
