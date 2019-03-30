import mr_streams as ms
import unittest

# :::: auxilary functions ::::
def repeat_n_times(x, n = 1):
    return [x] * n
def double(x):
    return [x,x]

class TestMisc(unittest.TestCase):

    def test_list_casting(self):
        _ = ms.stream([1,2,3,4,5]).flatmap(double)
        _ = list(_)
        _ = ms.stream([1, 2, 3, 4, 5]).flatmap(repeat_n_times, n = 2)
        _ = list(_)

    def test_next(self):
        _ = ms.stream([1,2,3,4,5]).flatmap(double)
        while next(_, None) is not None:
            continue
        _ = ms.stream([1, 2, 3, 4, 5]).flatmap(repeat_n_times, n = 2)
        while next(_, None) is not None:
            continue

    def test_for_loop(self):
        _ = ms.stream([1,2,3,4,5]).flatmap(double)
        _ = [x for x in _ ]
        _ = ms.stream([1, 2, 3, 4, 5]).flatmap(repeat_n_times, n = 2)
        _ = [x for x in _ ]

    def test_drain(self):
        _ = ms.stream([1,2,3,4,5]).flatmap(double)
        _.drain()
        _ = ms.stream([1, 2, 3, 4, 5]).flatmap(repeat_n_times, n = 2)
        _.drain()
