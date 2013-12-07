***************
Log file plugin
***************

This plugin logs all pages it recieves to a file.

It will append to an existing file in order to log.

Configuring the plugin
======================

Configuration for the plugin is done through the :file:`pagerprinter.ini` configuration file.

In order to activate the plugin, it must appear in the list of plugins.

.. code-block:: ini

	[pagerprinter]
	; Other plugins may be used as well, list them seperated by commas.
	plugins = logfile
	
	[logfile]
	; Full path to the file where you wish to log to
	filename = c:\pagerprinter\pages.txt
	
	; You must also specify how line feeds should be written in the log file.
	; If set to 1, this will write DOS-style linefeeds ("\r\n").
	; If set to 0, this will write UNIX-style linefeeds ("\n").
	crlf = 0

