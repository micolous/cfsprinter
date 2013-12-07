***************
Browser Support
***************

In order to print out a map to the location where the pager message references, you require a web browser that can print out on the commandline.

Only Mozilla Firefox is supported at this time.

Mozilla Firefox + cmdlnprint (``firefox``)
==========================================

In order to use the Firefox plugin, you need to set ``[pagerprinter]``.``browser`` to ``firefox``, and ``[pagerprinter]``.``browser-exec`` to the full path of Mozilla Firefox binary (or just ``firefox`` if it is in your ``PATH``:

.. code-block:: ini

	[pagerprinter]
	browser = firefox
	
	; On Linux, do this:
	browser-exec = firefox
	
	; On Mac OS X, you'll want something like this:
	browser-exec = /Applications/Firefox.app/Contents/MacOS/firefox-bin
	
	; On Windows, you'll want something like this:
	browser-exec = C:\Program Files\Mozilla Firefox\Firefox.exe
	
	; You may optionally specify a printer name.  If it is not specified, it
	; will use the system default printer.  On CUPS-based printing systems,
	; this is the printer's short name.  On Windows this is the full printer
	; name.
	printer = Father DeskLaser 934TXS
	
	; You can also print multiple copies.  By default only 1 is printed.
	print-copies = 1

You'll then need to `install the cmdlnprint extension`__ in Firefox.

__ http://sites.google.com/site/torisugari/commandlineprint2

There one tweakable option, the ``browser-wait`` setting.  This controls how many seconds to wait for the map to load before printing it out.

Disabling printing maps (``test``)
==================================

You can disable printing maps by setting ``browser`` to ``test``:

.. code-block:: ini

	[pagerprinter]
	browser = test
	
Instead of printing the maps, it will send the URI for the map to stdout.
