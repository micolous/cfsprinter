*****************
Huawei SMS Plugin
*****************

This plugin sends pages recieved as a text message via a Huawei USB 3G modem.

It has only been tested properly on Linux, and requires that the dongle be in "serial" mode.  This may require that you use ``usbmodeswitch`` to adjust the device.  Most Linux distributions do this automatically through ``udev``.

This plugin has a number of limitations:

* It will not create "concatenated" SMS for long messages -- instead it will send as many messages as needed to display the entire message
* It will not work with dongles that have their SIM card protected with a PIN without it being unlocked first (by another program).
* It will probably only work on Linux.

Configuring the plugin
======================

Configuration for the plugin is done through the :file:`pagerprinter.ini` configuration file.

In order to activate the plugin, it must appear in the list of plugins.

.. code-block:: ini

	[pagerprinter]
	; Other plugins may be used as well, list them seperated by commas.
	plugins = huaweisms
	
	[huaweisms]
	; This is a comma seperated list of phone numbers to send the SMS to.
	; This can be in local format or international format.
	to = 0491570110,+61491570156
	
	; This is the serial port that the Huawei dongle uses.
	; There are often 2 or 3 ports that the dongle assigns -- use the first of
	; those.
	port = /dev/ttyUSB0
