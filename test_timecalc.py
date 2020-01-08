#!/bin/sh

import unittest
import timecalc

class TestTime(unittest.TestCase):

    def test_counter(self):
        result = timecalc.counter(2, [0, 3], [1, 5])
        expected = 4
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()


#f = open("unittestresult.txt", "w")
#f.write("SUCCESS baby2")
#f.close()
#test
