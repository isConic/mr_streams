import mr_streams as ms
import unittest

# :::: auxilary functions ::::
def add_one(x):
    return x + 1

def tap_func(x):
    y = x + 1

class TestTap(unittest.TestCase):

    def test_list(self):
        _ = list(ms.stream([1, 2, 3, 4]).tap(tap_func))

    def test_next(self):
        _ = ms.stream([1, 2, 3, 4]).tap(tap_func)
        while next(_, None) is not None:
            continue

    def test_drain(self):
        _ = ms.stream([1, 2, 3, 4]).tap(tap_func)
        _.drain()