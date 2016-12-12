from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..attribute_selector_block import AttributeSelector


class TestExample(NIOBlockTestCase):

    def test_blacklist_signals(self):
        """The 'hello' signal attribute will get blacklisted"""
        blk = AttributeSelector()
        self.configure_block(blk, {'specify_behavior': 'BLACKLIST',
                                   'specify_attributes': ['hello']})
        blk.start()
        blk.process_signals([Signal({'hello': 'n.io', 'goodbye': 'n.io'})])
        blk.stop()
        self.assert_num_signals_notified(1)

        # should have blacklisted just hello
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
            {'goodbye': 'n.io'})

    def test_whitelist_signals(self):
        """'hello' attribute passes through the block unmodified."""
        blk = AttributeSelector()
        self.configure_block(blk, {'specify_behavior': 'WHITELIST',
                                   'specify_attributes': ['hello']})
        blk.start()
        blk.process_signals([Signal({'hello': 'n.io', 'goodbye': 'n.io'})])
        blk.stop()
        self.assert_num_signals_notified(1)

        # should have blacklisted the one incoming signal attribute
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
            {'hello': 'n.io'})

    def test_no_attributes_specified(self):
        """all signals pass through the block unmodified."""
        blk = AttributeSelector()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal({'hello': 'n.io'})])
        blk.stop()
        self.assert_num_signals_notified(1)

        # should have blacklisted the one incoming signal attribute
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
            {'hello': 'n.io'})
