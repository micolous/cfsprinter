#!/usr/bin/env python
"""
Display Plugin
Copyright 2015 Shane Rees <https://github.com/Shaggs/>

A Small GUI to display pager message on a screen. Will change from
Green > orange > Red at a 3 minute interval this way upon entering the
station you can have a ruff indication of response time.

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
    def execute(self, msg, unit, address, when, printer, print_copies):
        def orange():
            text_widget.config(bg="Orange")
            root.after(180000, red)
        def red():
            text_widget.config(bg="Red")
            root.after(180000, kill)
        def kill():
            root.destroy()
	mseg = str('%s - %s' % (msg, unit))
	root = Tk()
	text_widget = Text(root, font='times 40 bold', bg='Green')
	text_widget.pack(fill=BOTH, expand=0)
	text_widget.tag_configure('tag-center', wrap='word', justify='center')
	text_widget.insert(INSERT, "\n" + "\n"  +"\n" + mseg, 'tag-center')
	root.after(180000, orange)
	root.mainloop()		
PLUGIN = display
