AttributeSelector
=================

This block is used to whitelist or blacklist incoming signal attributes and notify 
the resulting modified signals.

Properties
--------------
-  Specify behavior: specify whitelist or blacklist behavior
-  Incoming signal attributes: specify any incoming signal attributes to ignore or allow depending on specified behavior


Whitelist:
----------------
The block will only emit those signals that are specified in the config.
If a specified attribute doesn't exist in the signal, it is ignored. 
If only invalid attributes are specified, a blank signal is notified.

Blacklist:
----------------
The block will emit all incoming attributes besides those specified in the
config. If a specified attribute doesn't exist in the signal, it is ignored.
If only invalid attributes are specified, the original signal is notified.


Dependencies
----------------
None

Commands
----------------
None

Input
-------
Any list of signals.

Output
---------
The input list of signals but with modified attributes.
