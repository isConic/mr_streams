import mr_streams as ms
import unittest
from operator import add

# :::: auxilary functions ::::
def add_one(x):
    return x + 1
def repeat_n_times(x, n = 1):
    return [x] * n
def double(x):
    return [x,x]

class TestMisc(unittest.TestCase):
    def test_001(self):
        _ = ms.stream([1,2,3,4,5])
        _ = _.map(add,1)\
                .map(add_one)\
                .flatmap( double)\
                .flatmap(repeat_n_times,  n = 2)
        _.drain()

    def test_embedded(self):
        stream_1 = ms.stream(range(10))
        stream_2 = ms.stream(stream_1)
        stream_3 = ms.stream(stream_2)
        stream_3.drain()