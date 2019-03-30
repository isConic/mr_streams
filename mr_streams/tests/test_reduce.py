import mr_streams as ms
import unittest

# :::: auxilary functions ::::
def sum_reduction(x,y):
    return x + y

class TestReduce(unittest.TestCase):

    def test_sum_reduce(self):
        _ = ms.stream([1,2,3,4,5]).reduce(sum_reduction)
        assert _ is 15

    def test_initializer(self):
        _ = ms.stream([1]).reduce(sum_reduction, initializer= 1)
        assert _ is 2

    def test_reduce_with_one_element(self):
        _ = ms.stream([1]).reduce(sum_reduction)
        assert _ is 1

    def test_empty_reduce(self):
        try:
            _ = ms.stream([]).reduce(sum_reduction)
        except ms.IllegalStreamOperationException:
            pass