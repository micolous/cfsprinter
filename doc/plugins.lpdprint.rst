************************
CUPS/LPD printing plugin
************************

This plugin prints the content of all pages.  This is different to the standard behaviour -- this doesn't print a map, it prints the page text itself.

This calls :program:`lpr` in order to do the actual printing.

This plugin only works on operating systems with CUPS (so Linux and Mac OS X).  Windows systems should use the :doc:`plugins.winprint` instead.

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
	printer = 934TXS
	
	; You can also print multiple copies.  By default only 1 is printed.
	print-copies = 1
	
	; You can control the size of the text with the following:
	; Number of characters per inch printed (lower numbers == wider text)
	; If not specified, this normally defaults to 10 characters per inch.
	print-cpi = 10
	
	; Number of lines per inch printed (lower numbers == taller text)
	; If not specified, this normally defaults to 6 lines per inch.
	print-lpi = 6
