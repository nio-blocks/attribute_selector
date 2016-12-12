from enum import Enum

from nio.signal.base import Signal
from nio.block.base import Block
from nio.properties import VersionProperty, SelectProperty, ListProperty
from nio.types import StringType


class Behavior(Enum):
    BLACKLIST = False
    WHITELIST = True


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
    specify_attributes = ListProperty(StringType,
                                      title='Incoming signal attributes',
                                      default=[])

    def __init__(self):
        super().__init__()
        self._specify_items = None

    def configure(self, context):
        super().configure(context)
        self._specify_items = set(spec for spec in
                                  self.specify_attributes())

    def process_signals(self, signals):
        self.logger.debug('specifying these attributes: {}'
                          .format(self._specify_items))

        new_sigs = []
        for signal in signals:
            sig_dict = signal.to_dict(include_hidden=True)
            specified_items = set(list(sig_dict.keys())).intersection(self._specify_items)

            if len(specified_items) == len(self._specify_items):
                if self.specify_behavior() is Behavior.WHITELIST:
                    self.logger.debug('whitelisting...')

                    new_sig = Signal({attr: sig_dict[attr] for attr in
                                      specified_items})

                    self.logger.debug('Allowing incoming attributes: {}'
                                      .format(specified_items))

                elif self.specify_behavior() is Behavior.BLACKLIST:
                    self.logger.debug('blacklisting...')

                    new_sig = Signal({attr: sig_dict[attr] for attr in sig_dict
                                      if attr not in specified_items})

                    self.logger.debug('Ignoring incoming attributes: {}'
                                      .format(specified_items))

                new_sigs.append(new_sig)
            else:
                self.logger.warning('specified an attribute that is not in the '
                                    'incoming signal: {} Notifying the original '
                                    'signal.'
                                    .format(self._specify_items.difference(specified_items)))

                new_sigs.append(signal)

        self.notify_signals(new_sigs)
