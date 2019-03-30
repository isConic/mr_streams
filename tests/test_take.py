import mr_streams as ms
import unittest
from operator import add

# :::: auxilary functions ::::
def add_one(x):
    return x + 1

def is_even(x):
    return x % 2 == 0

class TestMapFunction(unittest.TestCase):

    def test_take2_and_sum(self):
        _ = ms.stream([1,2,3,4]).map(add_one).take(2).reduce(add)
        assert _ is 5

    def test_take2_after_filter_and_sum(self):
        _ = ms.stream([1,2,3,4]).filter(is_even).take(2).reduce(add)
        assert _ is 6

    def test_take_more_than_you_have(self):
        _ = ms.stream([1,2,3,4]).take(5).reduce(add)
        assert _ is 10
