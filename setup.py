#!/usr/bin/env python
from setuptools import setup
from sys import version

try:
	import py2exe
except ImportError:
	print "Warning: py2exe is not installed."
	print "(Though it may not be available on your platform.)"

requires = ['win32api', 'configparser']
if version < '2.6.0':
	requires.append("simplejson")

setup(
	name='pagerprinter',
	version='0.1.4',
	author='Michael Farrell',
	url='http://github.com/micolous/cfsprinter',
	options=dict(py2exe=dict(includes=['plugins.winprint', 'plugins.lpdprint', 'plugins.skypesms', 'plugins.logfile'])),

	requires=requires,
	license='GPL3',
	console=[
		dict(script='py2exe_run.py', icon_resources=[(0, "pager.ico")]),
	],
	
	data_files=[('doc/pagerprinter', [
		'pagerprinter.example.ini',
		'README.md',
		'LICENSE.txt'
	])],
	package_dir={'pagerprinter': 'src/pagerprinter'},
	packages=['pagerprinter', 'pagerprinter.plugins', 'pagerprinter.scrapers'],
	entry_points={
		'console_scripts': [
			'pagerprinter = pagerprinter.pagerprinter:main',
		]
	}
)
