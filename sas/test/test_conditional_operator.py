import unittest
from ..conditional_operator import ConditionalOperator, ConditionalEffect

class TestConditoinalOperator(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_repr(self):
        name = 'a_asks_b'
        cost = 0
        prevail = {}
        cond_effs = [
                ConditionalEffect({16:0}, (32, -1, 0)),
                ConditionalEffect({16:0}, (34, -1, 0))
        ]
        cond_op = ConditionalOperator(name, cost, prevail, cond_effs)
        expected = ("begin_operator\n"
                    "a_asks_b\n"
                    "0\n"
                    "2\n"
                    "1 16 0 32 -1 0\n"
                    "1 16 0 34 -1 0\n"
                    "0\n"
                    "end_operator\n")
        self.assertEqual(str(cond_op), expected)
