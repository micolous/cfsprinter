"""
pyttsx (text to speech)
Copyright 2014 Shane Rees <https://github.com/Shaggs/>

This plug-in is designed to read out a copy of the received turnout
Page for those that maybe in the station or form those coming in
and need details.

it reads only parts of the page. They are RESPOND (job type), Alarm Level,
address, and any extra info after the ==

the speed is hard coded at this stage.



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
import pyttsx
import re
import time
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 100)
volume = engine.getProperty('volume')
engine.setProperty('volume', 100)


class TTS(BasePlugin):
	def execute(self, msg, unit, address, when, printer, print_copies):
		res = str('%s - %s' % (msg, unit))
		rem = re.compile('.*(RESPOND.*?ALARM\sLEVEL:\s\d)')
		resp = rem.match(res)
		more = str('%s - %s' % (msg, unit))
		inf = re.compile('.*==(.*?\s:)')
		info = inf.match(more)

		if resp:
			for group in resp.groups():
				if info:
					for group2 in info.groups():
						for x in range(3):
							engine.say(group)
							engine.say(group2)
							engine.runAndWait()
							time.sleep(180)
PLUGIN = TTS
