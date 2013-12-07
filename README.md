# pagerprinter #

A program to print out the South Australian Country Fire Service pager feeds.  It is written in an extensible way, so other backends can be plugged in to it.

Copyright 2011-2013 Michael Farrell <http://micolous.id.au/>

Version 0.1 (the prototype!).  This is incomplete, and contains bugs.

This package is not written or endorsed by the South Australian Country Fire Service.  While care has been taken while writing this application, it is created for informational purposes only and should not be relied upon in the event of an emergency.

**Documentation**: http://cfsprinter.rftd.org/

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

## Configuration ##

Configuration is done in pagerprinter.ini.  There is an example configuration
that is included.  You can start pagerprinter.py with a command line option of
what file you'd like to use settings from instead of pagerprinter.ini.

More information can be found in the [online documentation](http://cfsprinter.rtfd.org/).
