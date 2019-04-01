import mr_streams as ms
import unittest

# :::: auxilary functions ::::
def repeat_n_times(x, n = 1):
    return [x] * n
def double(x):
    return [x,x]

class TestChunk(unittest.TestCase):

    def test_chunk(self):
        _ = ms.stream([1,2,3,4,5]).chunk(2).drain()

    def test_less_than_n(self):
        _ = ms.stream([1,2,3,4,5]).chunk(6).drain()

    def test_empty(self):
        _ = ms.stream([]).chunk(6).drain()
