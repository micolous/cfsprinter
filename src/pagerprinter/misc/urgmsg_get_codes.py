#!/usr/bin/env python
"""
urgmsg_get_codes.py - script to grab currently used codes from urgmsg.net
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

from argparse import ArgumentParser
from urllib2 import urlopen
from bs4 import BeautifulSoup
import sqlite3


def main(database):
	print 'Getting current pages...'
	groups = {}

	for x in ('public', 'publicnosaas'):
	
		fp = urlopen('http://urgmsg.net/%s.php' % x)
		soup = BeautifulSoup(fp)
		
		
		for row in soup.find_all('tr'):
			address = int(row.select('td.COL1')[0].string)
			name = row.select('span.F')[0].string
			
			groups[address] = name.strip()
	
	# now dump these to the database
	print 'Got %d groups to dump...' % len(groups.items())
	
	dbo = sqlite3.connect(database)
	cur = dbo.cursor()
	
	for address, name in groups.items():
		try:
			cur.execute('INSERT INTO flexcodes VALUES (?, ?)', (address, name))
		except sqlite3.IntegrityError:
			# record already exists, skip
			pass
	
	dbo.commit()
	dbo.close()
	
	print 'Done!'
	
		
	
	
if __name__ == '__main__':
	parser = ArgumentParser()
	parser.add_argument('-d', '--database', required=True, help='Database file to use')
	
	options = parser.parse_args()
	main(options.database)