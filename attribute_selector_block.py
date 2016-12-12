from enum import Enum

from nio.signal.base import Signal
from nio.block.base import Block
from nio.properties import (VersionProperty, SelectProperty, ListProperty,
                            Property, PropertyHolder)


class Behavior(Enum):
    BLACKLIST = False
    WHITELIST = True


class SpecItem(PropertyHolder):
    item = Property(title='Attribute')


class AttributeSelector(Block):
    """
    A block for whitelisting or blacklisting incoming signals and notifying
    the rest.

    Properties:
    specify_behavior(select): select either whitelist or blacklist behavior
    specify_attributes(list): list of incoming signal attributes to blacklist
                              or whitelist
    """

    version = VersionProperty('1.0.0')
    specify_behavior = SelectProperty(Behavior, title='Specify behavior',
                                      default=Behavior.BLACKLIST)
    specify_attributes = ListProperty(SpecItem,
                                      title='Incoming signal attributes',
                                      default=[])

    def __init__(self):
        self._specify_items = None
        super().__init__()

    def start(self):
        self._specify_items = set(spec.item() for spec in
                                  self.specify_attributes())
        super().start()

    def process_signals(self, signals):
        self.logger.debug('specifying these attributes: {}'
                          .format(self._specify_items))

        for index, signal in enumerate(signals):
            sig_dict = signal.to_dict()

            specified_items = set(list(sig_dict.keys())).intersection(self._specify_items)

            if self.specify_behavior().value:
                # if true, whitelist behavior
                self.logger.debug('whitelisting...')

                popitems = []
                for item in sig_dict:
                    if item not in specified_items:
                        popitems.append(item)
                for item in popitems:
                    sig_dict.pop(item)

                self.logger.debug('Allowing incoming attributes: {}'
                                  .format(sig_dict))

            elif not self.specify_behavior().value:
                # if false, blacklist behavior
                self.logger.debug('blacklisting...')

                for item in specified_items:
                    sig_dict.pop(item)

                self.logger.debug('Ignoring incoming attributes: {}'
                                  .format(specified_items))
            else:
                self.logger.debug('invalid behavior type')
                return

            # replace signal with a signal minus the bad attributes
            signals[index] = Signal(sig_dict)

        self.notify_signals(signals)
