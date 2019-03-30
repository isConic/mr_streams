import mr_streams as ms
import unittest

# :::: auxilary functions ::::
from operator import add

class TestDrop(unittest.TestCase):


    def test_drop_less_than_list_length(self):
        _ = ms.stream([1, 2, 3, 4]).drop(2).reduce(add)
        assert _ == 7

    def test_drop_more_than_list_length(self):
        _ = ms.stream([1, 2, 3]).drop(4).drain()
