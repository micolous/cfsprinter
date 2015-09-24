#!/usr/bin/env python
"""
Huawei SMS plugin
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
import serial, time


# make our plugin!
class HuaweiSmsPlugin(BasePlugin):
	def configure(self, c):
		# read in phone numbers we need
		self.numbers = [
			x.strip()
			for x
			in c.get('huaweisms', 'to').lower().split(',')
		]

		self.ser = serial.Serial(c.get('huaweisms', 'port'), 460800, timeout=5)

	def execute(self, msg, unit, address, when, printer, print_copies):
		sms = str('%s - %s' % (msg, unit))

		for x in range(0, len(sms), 150):
			for phone_number in self.numbers:
				self.ser.write('ATZ\r')
				time.sleep(1)
				self.ser.write('AT+CMGF=1\r')
				time.sleep(1)
				self.ser.write('AT+CMGS="%s"\r' % str(phone_number))
				time.sleep(1)
				self.ser.write(sms[x:x + 150] + '\r' + chr(26))
				time.sleep(1)
				print "Sent mesage to %r: %r" % (phone_number, sms)


PLUGIN = HuaweiSmsPlugin
