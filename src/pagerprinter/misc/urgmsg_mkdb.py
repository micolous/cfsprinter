#!/usr/bin/env python
"""
urgmsg_get_codes.py - script to grab currently used codes from urgmsg.net
Copyright 2010 - 2015 Michael Farrell <http://micolous.id.au/>

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
from ..scrapers.sacfs_flexcode import CODES
from argparse import ArgumentParser
import sqlite3


def main(database):
	dbo = sqlite3.connect(database)

	# create our table
	cur = dbo.cursor()
	cur.execute("""
		CREATE TABLE IF NOT EXISTS flexcodes (
			address INTEGER PRIMARY KEY,
			name TEXT
		)
	""")

	for address, name in CODES.items():
		cur.execute('DELETE FROM flexcodes WHERE address = ?', (address,))
		cur.execute('INSERT INTO flexcodes VALUES (?, ?)', (address, name.strip()))

	dbo.commit()
	dbo.close()

	print 'Done!'

if __name__ == '__main__':
	parser = ArgumentParser()
	parser.add_argument('-d', '--database', required=True, help='Database file to use')

	options = parser.parse_args()
	main(options.database)
