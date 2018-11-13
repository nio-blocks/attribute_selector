AttributeSelector
=================
The AttributeSelector block is used to whitelist or blacklist incoming signal attributes. Whitelisted attributes will be included in the outgoing signal. Blacklisted attributes will be excluded from the outgoing signal.

Properties
---
- **Incoming Signal Attributes**: The name (plain text string) of the signal attribute to whitelist or blacklast depending on the **Selector Mode**.
- **Selector Mode**: Specify whitelist or blacklist behavior for the selected incoming signal attribute(s).

Outputs
---
The incoming list of signals but with attributes modified according to the whitelist/blacklist selections.

Blacklist
---
The block will emit all incoming attributes besides those specified in the `Incoming Signal Attributes`configuration. If a specified attribute doesn't exist in the signal, it is ignored. If only invalid attributes are specified, the original signal is notified.

Whitelist
---
The block will only emit those signals that are specified in the `Incoming Signal Attributes`configuration. If a specified attribute doesn't exist in the signal, it is ignored. If only invalid attributes are specified, a blank signal is notified.
