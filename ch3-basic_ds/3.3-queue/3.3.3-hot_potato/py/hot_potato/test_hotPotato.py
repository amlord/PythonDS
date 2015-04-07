from unittest import TestCase
from hot_potato import hotPotato

__author__ = 'Lawrence'


class TestHotPotato(TestCase):
    def test_hotPotato(self):
        self.assertEqual(
            hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],0),
            "Brad",
            "The survivor of calling to hotPotato(['Bill','David','Susan'," +
            "'Jane','Kent','Brad'],0) is not 'Bill'.")
        self.assertEqual(
            hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],1),
            "Kent",
            "The survivor of calling to hotPotato(['Bill','David','Susan'," +
            "'Jane','Kent','Brad'],0) is not 'Kent'.")
        self.assertEqual(
            hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7),
            "Susan",
            "The survivor of calling to hotPotato(['Bill','David','Susan'," +
            "'Jane','Kent','Brad'],0) is not 'Susan'.")