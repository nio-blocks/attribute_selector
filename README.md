AttributeSelector
=================
The AttributeSelector block is used to whitelist or blacklist incoming signal attributes. The block will alter the signal based on which attributes are allowed and emit the modified signal.

Properties
----------
- **attributes**: Incoming signal attributes to ignore or allow depending on whether whitelist or blacklist is chosen as the Selector Mode.
- **mode**: Specify whitelist or blacklist behavior.

Inputs
------
- **default**: Any list of signals

Outputs
-------
- **default**: The input list of signals but with modified attributes depending on whitelist/blacklist selections.

Commands
--------
None

Blacklist:
----------
The block will emit all incoming attributes besides those specified in the
config. If a specified attribute doesn't exist in the signal, it is ignored.
If only invalid attributes are specified, the original signal is notified.

Dependencies
------------
None

Whitelist:
----------
The block will only emit those signals that are specified in the config.
If a specified attribute doesn't exist in the signal, it is ignored.
If only invalid attributes are specified, a blank signal is notified.

