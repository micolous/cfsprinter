***************
Mapping Support
***************

When printing maps, you can use a couple of different providers.  This is configurable with the ``[pagerprinter]]``.``mapper`` option in :file:`pagerprinter.ini`.

You will need to also set your "home address" for the routing to work.

.. code-block:: ini

	[pagerprinter]
	home = 175 Waymouth Street, Adelaide, South Australia
	mapper = google

Google Printer-friendly (``google``)
====================================

This handler uses the printer-friendly maps on the Google Maps website to make a list of directions.  It only has text on it.

Google Screen (``googlescreen``)
================================

This handler uses the screen / display version of the Google Maps website, to show the route with images and text.

It doesn't fit as well onto a page, but shows a bigger map.

Other mapping options under investigation
=========================================

Bing Maps
---------

Supplies API and website.  It doesn't generate nice printer-friendly URIs like Google Maps.  API requires registration and access keys.

Australian mapping source for Bing isn't very good, and has many errors (such as listing certain PoIs by a name that hasn't been used in over 40 years, missing roads, and listing private roads as thoroughfares).

OpenStreetMaps
--------------

Doesn't provide a router (for directions), so will require running your own route server.

Coverage varies greatly.  Most roads are in the map but are often not labelled by name.

Mapping sites that will never work
==================================

Whereis
-------

Provides no public (free) API.  Searches are saved in a database by ID, then this is recalled with some funky JavaScript and referrer tricks in order to generate printer-friendly views.

Sensis/Whereis data has been incorporated into Google Maps in many parts (which is much more accessible), so isn't a great loss.

Yahoo
-----

Does not provide navigation.
