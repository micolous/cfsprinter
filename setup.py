from distutils.core import setup
from sys import version
try:
	import py2exe
except ImportError:
	print "Warning: py2exe is not installed.  (Though it may not be available on your platform.)"

requires = ['win32api']
if version < '2.6.0':
	requires.append("simplejson")

setup(
	name='cfsprinter',
	version='0.1.1',
	author='Michael Farrell',
	url='http://github.com/micolous/cfsprinter',
	py_modules=['browsersupport', 'mappingsupport', 'pagerscraper', 'pagerprinter'],
	packages=['plugins'],
	includes=['plugins.winprint', 'plugins.lpdprint'],
	data_files=[
		('doc', [
			'pagerprinter.example.ini',
			'README.txt',
			'LICENSE.txt'
		]),
		# UGLY HACK
		('plugins', [
			'plugins/winprint.py',
			'plugins/lpdprint.py'
		]),
	],
	requires=requires,
	license='GPL3',
	console=['pagerprinter.py']
)
