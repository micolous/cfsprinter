#!/usr/bin/env python
"""
Test program for pager feed sources
Copyright 2010 - 2013 Michael Farrell <http://micolous.id.au/>

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
import argparse
from . import get_scraper

parser = argparse.ArgumentParser()
parser.add_argument('feed', metavar='FEED', nargs=1, help='Pager function to test')
parser.add_argument('--update-frequency', metavar='SECS', default=30, type=int, help='Number of seconds to wait before updating again [default: %(default)s]')

options = parser.parse_args()

def test_handler(good_parse, **message):
	print "msg = %s" % message

print "Activating test program for %r..." % options.feed
print "(Press ^C to quit)"
scraper = get_scraper(options.feed[0])(update_frequency=options.update_frequency)
scraper.update_forever(test_handler)
