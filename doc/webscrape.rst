**********************************
Using with a web-based paging feed
**********************************

The regular mode of operation of pagerprinter is to use a web-based paging feed.  This scrapes from the AJAX update functionality of urgmsg.net and sacfs.org's pager feeds.

This requires an internet connection, and polls the servers by default every 30 seconds.  This is in many cases slower than their own JavaScript updates their paging feed, so causes less load than leaving the web page open.

If you can, use this software with a local scanner and PDW, as it causes no load on these servers and updates quicker.  You can read more about this option in :doc:`pdw`.


Configuring pagerprinter
========================

In order to use PDW, the ``[pagerprinter]`` ``backend`` setting must be set:

.. code-block:: ini

	[pagerprinter]
	; To use paging1.sacfs.org (primary server)
	backend = sacfs
	
	; To use paging2.sacfs.org
	backend = sacfs2
	
	; To use paging3.sacfs.org
	backend = sacfs3
	
	; To use urgmsg.net
	backend = sacfs-urgmsg
	
	; Set the update frequency to every 30 seconds.  If you don't need it,
	; you should increase this duration so it updates less frequently.
	update-frequency = 30

