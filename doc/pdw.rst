**************
Using with PDW
**************

`PDW is a pager decoder software`__.  It can be used in conjunction with ``pagerprinter`` to recieve pages "over the air" (ie: without an internet connection) from the SAGRN service.

It will require connecting an appropriate radio's discriminator output, tuned to ``148.8125 MHz``, to the input of a sound card attached to your computer.

The module makes no allowances for errors in the pages received, so you will need to ensure that you have a good signal.  Corrupted pages will not be parsed correctly.

.. note:: This module is currently under development and does not yet recognise all pager group addresses (flex codes / cap codes).  This is required in order to be able to know which station a page is for.

__ http://www.discriminator.nl/pdw/index-en.html

Configuring pagerprinter
========================

In order to use PDW, the ``[pagerprinter]`` ``backend`` setting must be set to ``sacfs-pdw``:

.. code-block:: ini

	[pagerprinter]
	backend = sacfs-pdw

There are no other configuration options currently available for this scraper.

The ``update-frequency`` setting has no effect -- all pages will be passed asynchronously as soon as they are received.

Configuring the radio
=====================

The radio will need to be tuned to the SAGRN pager frequency, ``148.8125 MHz`` FM.

The discriminator output of the radio will need to be attached to your computer's line-in jack.  Most radios do not provide a direct discriminator output, and `will require some soldering and circuitry in order to access it`__.  This is outside of the scope of this document.

__ http://www.discriminator.nl/index-en.html

Once this is complete, you should be able to hear through the line-in jack, pager data at least once every minute, and static between pages (when there is no carrier).

The audio must through the left audio channel, as this is the channel used by PDW.  It does not matter if it also comes through the right audio channel, as long as it is also coming through the left.

Configuring PDW
===============

In PDW, it will need to be configured to decode FLEX 1600 pages.  You will also need to configure PDW to receive pages from a sound card (it defaults to a serial device).

You should be able to see the pages as they come in on the main screen of PDW, with minimal data errors (these are shown in light red -- correct data is shown in cyan).  If you don't, there may be issues with your audio levels or insufficient signal strength in your location.

About once every minute there should be a page on your screen for FLEX address ``1900253``, which are test pages.  They should give you an easy way to test various settings and antenna configurations.

Once the configuration is verified as working, you can then setup the link between pagerprinter and PDW.

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

