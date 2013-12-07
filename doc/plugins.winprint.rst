***********************
Windows printing plugin
***********************

This plugin prints the content of all pages.  This is different to the standard behaviour -- this doesn't print a map, it prints the page text itself.

This plugin calls the default text ``print`` action in order to print the page (normally this is Notepad).  Therefore text formatting is configurable by changing Notepad's settings.

This plugin only works on Windows.  CUPS-based systems should use the :doc:`plugins.lpdprint` instead.

Configuring the plugin
======================

Configuration for the plugin is done through the :file:`pagerprinter.ini` configuration file.

In order to activate the plugin, it must appear in the list of plugins.

This uses the same printer configuration as the main mapping part of the application.

.. code-block:: ini

	[pagerprinter]
	; Other plugins may be used as well, list them seperated by commas.
	plugins = winprint
	
	; This shares the same print setting as the rest of the application.
	; If not specified, this will use the system default printer.
	printer = Father DeskLaser 934TXS
	
	; You can also print multiple copies.  By default only 1 is printed.
	print-copies = 1

