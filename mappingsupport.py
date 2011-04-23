#!/usr/bin/env python
"""
Maps backend support code for pagerprinter.
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
from urllib import urlencode

class GoogleMaps(object):
	def get_url(self, start, finish):
		return u'http://maps.google.com.au/maps?%s' % urlencode((('f', 'q'), ('saddr', start), ('daddr', finish), ('pw', '2')))

class GoogleMapsScreen(object):
	def get_url(self, start, finish):
		return u'http://maps.google.com.au/maps?%s' % urlencode((('f', 'q'), ('source', 's_d'), ('saddr', start), ('daddr', finish)))


MAP_MAP = {
	'google': GoogleMaps,
	'gmaps': GoogleMaps,
	'googlemaps': GoogleMaps,
	'googlescreen': GoogleMapsScreen,
	'googlemapsscreen': GoogleMapsScreen,
	'gmapscreen': GoogleMapsScreen,
}

def get_map(name):
	name = name.lower().strip()
	return MAP_MAP[name]()


