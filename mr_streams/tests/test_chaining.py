import mr_streams as ms
import unittest

# :::: auxilary functions ::::
def add_one(x):
    return x + 1

def triplicate(x):
    return (x,x,x)

def no_op(*args, **kwargs):
    pass

class TestChaining(unittest.TestCase):

    def test_MaFiTaFlTkTpDr(self):
        _ = ms.stream(range(20))

        _.map(add_one)\
            .filter(lambda x: x%2 == 0)\
            .take(3)\
            .flatmap(triplicate)\
            .take(8)\
            .tap(no_op)

        _.drain()