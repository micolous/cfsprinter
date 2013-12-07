**************
Using with PDW
**************

`PDW is a pager decoder software`__.  It can be used in conjunction with ``pagerprinter`` to recieve pages "over the air" (ie: without an internet connection).

It will require connecting an appropriate radio tuned to ``148.8125 MHz`` to a sound card attached to your computer.

The module makes no allowances for errors in the pages received, so you will need to ensure that you have a good signal.  Corrupted pages will not be parsed correctly.

.. note:: This module is currently under development and does not yet recognise all pager group addresses (flex codes / cap codes).  This is required in order to be able to know which station a page is for.

__ http://www.discriminator.nl/pdw/index-en.html

Configuring pagerprinter
========================

In order to use PDW, the ``[pagerprinter]``.``backend`` setting must be set to ``sacfs-pdw``:

.. code-block:: ini

	[pagerprinter]
	backend = sacfs-pdw

There are no other configuration options currently available for this scraper.

The ``update-frequency`` setting has no effect -- all pages will be passed asynchronously as soon as they are received.

Configuring PDW
===============

Configuring PDW to receive pages successfully is outside of the scope of this document.  At this point is is assumed that you are already able to receive pages reliably and pages are showing inside of PDW.

When using the ``sacfs-pdw`` scraper in ``pagerprinter``, it will run an SMTP server bound to ``localhost:8825``.  PDW can then send emails to this server and this will generate events inside of ``pagerprinter``.

It does not require an email account to use or an active internet connection.  The messages will be entirely confined to your own computer -- SMTP is merely used as a way to pass messages around.

In order to configure PDW to propegate pages to pagerprinter:

1. :menuselection:`Options --> SMTP/Email...`
2. Tick :guilabel:`Enable Email Notification`.
3. Set :guilabel:`Setting` to :guilabel:`All messages`.
4. Set :guilabel:`Port` to ``8825``.
5. Set :guilabel:`SMTP Host` to ``localhost``.
6. Make sure :guilabel:`Enable Authentication` is not ticked.
7. In :guilabel:`Mail options`, tick only :guilabel:`Address`, :guilabel:`Time`, :guilabel:`Date` and :guilabel:`Message`.
8. Set :guilabel:`Notification` to :guilabel:`Message`.
9. Set the :guilabel:`To` and :guilabel:`From` email addresses to a valid email address.  It won't be used for sending mail.

Adding more pager group addresses
=================================

.. note:: In order to use these scripts, you will require ``libsqlite3 >= 3.7.15``.  ``libsqlite3`` is not required for any other functionality in ``pagerprinter``, even when using PDW.

	On Debian systems this is in the ``libsqlite3-0`` package, and ``wheezy`` has an old version (you will need at least ``jessie``)

	The versions of ``libsqlite3`` included with Python 2.7 on Windows platforms are old and require manual replacement:
	
	On ``win32`` (and x86_32 versions of Python running on ``x86_64`` versions of Windows), you can `download the precompiled version of sqlite3.dll from the SQLite website`__, overwriting :file:`C:\\Python27\\DLLs\\sqlite3.dll`.

	On ``x86_64`` (using an ``x86_64`` version of Python), download :file:`sqlite-netfx40-static-binary-x64-2010-{*}.zip` `from the System.Data.Sqlite website`__, and overwrite :file:`C:\\Python27\\DLLs\\sqlite3.dll` with :file:`SQLite.Interop.dll` from that archive.

__ https://www.sqlite.org/download.html
__ http://system.data.sqlite.org/index.html/doc/trunk/www/downloads.wiki

Pager group addresses (flex codes / cap codes) are stored in :file:`src/pagerprinter/scrapers/sacfs_flexcode.py`, in the :py:const:`pagerprinter.scrapers.sacfs_flexcode.CODES` dict.

In order to start working on managing the codes, you will need to dump the existing codes to a sqlite database:

.. code-block:: console

	$ python -m pagerprinter.misc.urgmsg_mkdb -d codes.db3

This will create a file called :file:`codes.db3` in the current directory with the existing codes that are in :file:`sacfs_flexcode.py`.  Any conflicting codes will be overwritten.

You can then scrape the ``urgmsg.net`` site for new codes with:

.. code-block:: console

	$ python -m pagerprinter.misc.urgmsg_get_codes -d codes.db3

Once you have new codes, you can then output that back to :file:`sacfs_flexcode.py` with:

.. code-block:: console

	$ python -m pagerprinter.misc.urgmsg_export_codes -d codes.db3 -o src/pagerprinter/scrapers/sacfs_flexcode.py

