from enum import Enum

from nio.signal.base import Signal
from nio.block.base import Block
from nio.properties import (VersionProperty, SelectProperty, ListProperty,
                            Property, PropertyHolder)


class IgnoreChoice(Enum):
    BLACKLIST = False
    WHITELIST = True


class IgnoreItem(PropertyHolder):
    item = Property(title='Attribute')


class IgnoreSignals(Block):
    """
    A block for whitelisting or blacklisting incoming signals and notifying
    the rest.

    Properties:
    ignore_behavior(select): select either whitelist or blacklist behavior
    ignore_items(list): list of incoming signal attributes to ignore
    """

    version = VersionProperty('1.0.0')
    ignore_behavior = SelectProperty(IgnoreChoice, title='Ignore behavior',
                                     default=IgnoreChoice.BLACKLIST)
    ignore_items = ListProperty(IgnoreItem, title='Attributes to ignore',
                                default=[])

    def __init__(self):
        self._ignore = None
        super().__init__()

    def start(self):
        self._ignore = set(ignore.item() for ignore in self.ignore_items())
        super().start()

    def process_signals(self, signals):
        self.logger.debug('self._ignore: {}'.format(self._ignore))
        for index, signal in enumerate(signals):
            sig_dict = signal.to_dict()

            specified_items = set(list(sig_dict.keys())).intersection(self._ignore)

            if self.ignore_behavior() == True:
                # if true, whitelist behavior
                self.logger.debug('whitelisting...')

                for item in sig_dict:
                    if item not in specified_items:
                        sig_dict.pop(item)
            else:
                # if false, blacklist behavior
                self.logger.debug('blacklisting...')

                for item in specified_items:
                    sig_dict.pop(item)

                self.logger.debug('Ignoring incoming attributes: {}'
                                  .format(specified_items))

            # replace signal with a signal minus the bad attributes
            signals[index] = Signal(sig_dict)

        self.notify_signals(signals)
