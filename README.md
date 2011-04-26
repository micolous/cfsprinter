# pagerprinter #

A program to print out the South Australian Country Fire Service pager feeds.  It is written in an extensible way, so other backends can be plugged in to it.

Copyright 2011 Michael Farrell <http://micolous.id.au/>

Version 0.1 (the prototype!).  This is incomplete, and contains bugs.

## Licensing ##

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

## Requirements ##

 * Python 2.6 or later.  Python 2.5 may work with the simplejson package installed.
 * On Windows, the Python win32all package.  http://sourceforge.net/projects/pywin32/
 * On Firefox, the cmdlnprint extension.  http://sites.google.com/site/torisugari/commandlineprint2

## Getting It ##

The source code for the program is available at https://github.com/micolous/cfspager/

A git repository of the latest code is available at git://github.com/micolous/cfspager.git

## Configuration ##

Configuration is done in pagerprinter.ini.  There is an example configuration
that is included.  You can start pagerprinter.py with a command line option of
what file you'd like to use settings from instead of pagerprinter.ini.

## Browser Support ##

Only Firefox / Iceweasel is supported at the moment.  You'll need the extension cmdlnprint installed.  You can get this from http://sites.google.com/site/torisugari/commandlineprint2

On Windows, you'll need to set the full path to Firefox in the "browser-exec" setting.

## Mapping Support ##

The following mapping backends are available:

 * google: Prints out a text-based map of directions from Google Maps AU.  Google will try to replace location names in searches, which can be misleading, and sometimes entirely messes up directions including location names.  This is the default option.
 * googlescreen: Same as `google`, except with the graphical, non-printer-friendly map (like the one you normally see in your browser).

Some other mapping options under investigation:

 * bing: Supplies API, supplies website.  It doesn't seem easy to generate printer-friendly maps from the site like I can with Google Maps.  API requires access keys and registration.
 * osm: Doesn't provide routers (will require running a route server).

Mapping sites that are impossible:

 * whereis: Provides no public (free) API, generates "shortlinks" (ie: it saves your searches into a database, and it is assigned an ID) and uses interesting referrer and Javascript tricks in order to generate printer-friendly pages.  Sensis/Whereis data is used on Google Maps anyway (which is much more accessible), so not a great loss.
 * yahoo: Doesn't provide navigation.

## Plugins ##

There are two plugins included:

 * lpdprint: Prints the page as text on Linux and Mac OS X.  It uses the command-line lpr utility, and has been tested only using CUPS (not actual LPD).  This probably works on Windows too, if you're using Cygwin (or have lpr).
 * winprint: Prints the page as text on Windows.  This requires the win32all package.


## TODO ##

 * Fix google maps backend so it works with images.
 * Add other mapping backends.
 * Add other browser backends.
 * ???
 * Testing...

