#!/usr/bin/env python
"""
Maps backend support code.
"""
from urllib import urlencode

class GoogleMaps(object):
	def get_url(self, start, finish):
		return u'http://maps.google.com.au/maps?%s' % urlencode((('f', 'q'), ('saddr', start), ('daddr', finish), ('pw', '2')))


MAP_MAP = {
	'google': GoogleMaps,
	'gmaps': GoogleMaps,
	'googlemaps': GoogleMaps,
}

def get_map(name):
	name = name.lower().strip()
	return MAP_MAP[name]()


