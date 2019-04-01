import mr_streams as ms
import unittest


class TestWindow(unittest.TestCase):

    def test_window_doesnt_break(self):
        _ = ms.stream(range(10)).window(n = 2).drain()

    def test_larger_stride_than_window_doesnt_break(self):
        _ = ms.stream(range(10)).window(n = 2, stride = 4).drain()

    def test_larger_window_than_stream_doesnt_break(self):
        _ = ms.stream(range(5)).window(n = 10).drain()

    def test_larger_stride_than_stream_doesnt_break(self):
        _ = ms.stream(range(5)).window(n = 2, stride= 10).drain()

    def test_n2_window_works_to_specification(self):
        stream = ms.stream(range(10)).window(n = 2)

        computed = [*stream]
        expected = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9)]

        assert computed == expected

    def test_n2_s2_window_works_to_spec(self):
        stream = ms.stream(range(10)).window(n=2, stride= 2)

        computed = [*stream]
        expected = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]

        assert computed == expected

    def test_n2_s3_window_works_to_spec(self):
        stream = ms.stream(range(10)).window(n=2, stride= 3)

        computed = [*stream]
        expected = [(0, 1), (3, 4), (6, 7), (9)]

        assert computed == expected

    def test_assumptions_about_list_equality(self):
        a = [1,2,3,4]
        b = [1,2,3,4]
        assert a == b

        a = [(1,1), (2,2), (3,3)]
        b = [(1,1), (2,2), (3,3)]
        assert a == b

