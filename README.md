AttributeSelector
=================
The AttributeSelector block is used to whitelist or blacklist incoming signal attributes. Whitelisted attributes will be included in or blacklisted attributes will be excluded from the outgoing signal.

Properties
----------
- **attributes**: Incoming signal attributes to either include or exclude, depending on whether whitelist or blacklist is chosen as the **selector mode**.
- **mode**: Specify whitelist or blacklist behavior.

Inputs
------
- **default**: Any list of signals

Outputs
-------
- **default**: The incoming list of signals but with attributes modified according to the whitelist/blacklist selections.

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

