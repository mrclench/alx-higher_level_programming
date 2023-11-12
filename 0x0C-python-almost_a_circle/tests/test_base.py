#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_default_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_incrementing_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_mixed_ids(self):
        b1 = Base()
        b2 = Base(5)
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 5)
        self.assertEqual(b3.id, 2)

if __name__ == '__main__':
    unittest.main()
