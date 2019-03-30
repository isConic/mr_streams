import mr_streams as ms
import unittest
from operator import add

# :::: auxilary functions ::::
def add_one(x):
    return x + 1

class TestMapFunction(unittest.TestCase):

    def test_compose_a_map(self):
        _ = ms.stream([1,2,3,4]).map(add_one)
        _ = ms.stream([1,2,3,4]).map(add, 1)

    def test_map_to_list(self):
        _ = list( ms.stream([1,2,3,4]).map(add_one))
        _ = list( ms.stream([1,2,3,4]).map(add, 1))

    def test_next_from_map(self):
        _ = ms.stream([1, 2, 3, 4]).map(add_one)
        while next(_, None) is not None:
            continue

        _ = ms.stream([1, 2, 3, 4]).map(add, 1)
        while next(_, None) is not None:
            continue

    def test_drain_a_map(self):
        _ = ms.stream([1,2,3,4]).map(add_one)
        _.drain()

        _ = ms.stream([1,2,3,4]).map(add, 1)
        _.drain()

