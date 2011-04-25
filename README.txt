Program to automatically print out CFS pager feeds.
Copyright 2011 Michael Farrell <http://micolous.id.au/>

Version 0.1 (the prototype!)

This is incomplete, and contains bugs.

== Licensing ==

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

== Requirements ==

 * Python 2.6 or later.  Python 2.5 may work with the simplejson package installed.
 * On Windows, the Python win32all package.  http://sourceforge.net/projects/pywin32/
 * On Firefox, the cmdlnprint extension.  http://sites.google.com/site/torisugari/commandlineprint2
 

== Configuration ==

Configuration is done in pagerprinter.ini.  There is an example configuration
that is included.  You can start pagerprinter.py with a command line option of
what file you'd like to use settings from instead of pagerprinter.ini.


== Browser Support ==

Only Firefox / Iceweasel is supported at the moment.  You'll need the extension
cmdlnprint installed.  You can get this from 
http://sites.google.com/site/torisugari/commandlineprint2

On Windows, you'll need to set the full path to Firefox in the "browser-exec" setting.

== Mapping Support ==

The following mapping backends are available:

 * google: Prints out a text-based map of directions from Google Maps AU.
 * googlescreen: Prints out the graphical, non-printer-friendly map from Google Maps AU.


== Plugins ==

There are two plugins included:

- lpdprint: Prints the page as text on Linux and Mac OS X.  It uses the command-line lpr utility, and has been tested only using CUPS (not actual LPR).
- winprint: Prints the page as text on Windows.  This requires the win32all package.


TODO::

- Fix google maps backend so it works with images.
- Add other mapping backends.
- Add other browser backends.
- ???
- Testing...

