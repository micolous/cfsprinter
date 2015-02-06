#!/usr/bin/env python
"""
Display Plugin
Copyright 2015 Shane Rees <https://github.com/Shaggs/>

A Small GUI to display pager message on a screen 

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
import os, sys
import time
from Tkinter import *


class display(BasePlugin):
	def _close():
		root.destroy()
		
	def execute(self, msg, unit, address, when, printer, print_copies):
		mseg = str('%s - %s' % (msg, unit))
		root = Tk()
		text = Text(root, wrap = 'word', bg= 'red', font= 'times 30 bold')
		text.insert(INSERT, msg)
		text.pack(anchor= 'sw', fill = 'both', expand = 'yes')
		root.title('Pager Printer Display')
		root.after(6000, root.destroy)
		root.mainloop(0)
		
PLUGIN = display
