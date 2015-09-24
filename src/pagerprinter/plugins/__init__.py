#!/usr/bin/env python
"""
Plugin support code for pagerprinter.
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
from sys import modules


class BasePlugin(object):
	def configure(self, config):
		"""\
Passes ConfigParserPlus instance to plugins so that they can be configured.  By
default this does nothing.
"""
		pass

	def execute(self, msg, unit, address, when, printer, print_copies):
		"""Executed when there is a new message matching filters"""
		print "WARNING: BasePlugin default execute called!"
		print "- Message: %s" % msg
		print "- Unit: %s" % unit
		print "- Address: %s" % address
		print "- When: %s" % when
		print "- Printer: %s" % printer
		print "- Copies: %s" % print_copies


def get_plugin(name):
	name = 'pagerprinter.plugins.' + name.lower().strip()
	__import__(name)
	return modules[name].PLUGIN()
