import mr_streams as ms
import unittest

# :::: auxilary functions ::::
def add_one(x):
    return x + 1

class TestBareStream(unittest.TestCase):

    def test_list_casting(self):
        _ = list(ms.stream([1, 2, 3, 4]))

    def test_next(self):
        _ = ms.stream([1, 2, 3, 4])
        while next(_, None) is not None:
            continue

    def test_drain(self):
        _ = ms.stream([1, 2, 3, 4])
        _.drain()

    def test_cast_to_iter(self):
        _ = ms.stream([1, 2, 3, 4])
        _ = iter(_)