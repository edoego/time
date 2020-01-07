#!/bin/sh

import unittest
import time

class TestTime(unittest.TestCase):

    def test_counter(self):
        result = time.counter(2, [0,3], [1,5])
        self.assertEqual(result, 4)





#f = open("unittestresult.txt", "w")
#f.write("SUCCESS baby")
#f.close()
#test
