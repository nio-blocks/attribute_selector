AttributeSelector
=================
The AttributeSelector block is used to whitelist or blacklist incoming signal attributes. Whitelisted attributes will be included in the outgoing signal. Blacklisted attributes will be excluded from the outgoing signal.

Properties
---
- **Incoming Signal Attributes**: The name of the signal attribute (entered into the block configuration as a string, no `{{$}}` required) to whitelist or blacklist.
- **Selector Mode**: Specify whitelist or blacklist behavior for the selected `Incoming Signal Attributes`.

Outputs
---
The incoming list of signals but with attributes modified according to the whitelist or blacklist selection.

Blacklist
---
The block will notify all incoming attributes besides those specified in the `Incoming Signal Attributes` configuration. If a specified attribute doesn't exist in the signal, it is ignored. If only invalid attributes are specified, the original signal is notified.

Whitelist
---
The block will only notify those signals that are specified in the `Incoming Signal Attributes`configuration. If a specified attribute doesn't exist in the signal, it is ignored. If only invalid attributes are specified, an empty signal is notified.
