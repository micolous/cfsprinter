#!/usr/bin/env python
"""
Library to scrape events from emergency services pager feeds.
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

__all__ = ['get_scraper']


# TODO: make this dynamic.
from .sacfs import *

SCRAPER_MAP = {
	'sacfs': CFSPagerScraper,
	'sacfs-urgmsg': CFSPagerUrgmsgScraper
}


def get_scraper(name):
	name = name.lower().strip()
	return SCRAPER_MAP[name]


