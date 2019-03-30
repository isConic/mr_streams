from functools import partial, reduce
from  mr_streams.exceptions import IllegalStreamOperationException

class EOL():
    pass

class Streamer:
    def __init__(self, _iter):
        self.structure = iter(_iter)
        self.eol = EOL()

    def _build(self, expression):
        self.structure = expression
        self.structure = iter(self.structure)
        return self

    def __iter__(self):
        return self

    def __next__(self):
        _obj = next(self.structure, self.eol)
        if _obj is not self.eol:
            return _obj
        else:
            raise StopIteration

    def _flatten(self, _generator,_function):
        yield from (y for x in _generator for y in _function(x))

    def map(self, _function, *args, **kwargs):
        _curried_function = partial(_function, *args, **kwargs)
        return self._build(map(_curried_function, self.structure))

    def flatmap(self, _function, *args, **kwargs):
        _curried_function = partial(_function, *args, **kwargs)
        return self._build(self._flatten(self.structure, _curried_function))

    def reduce(self, _function, initializer = None, *args, **kwargs):
        struct = iter(self.structure)
        a = next(struct, self.eol)
        if a is self.eol:
            raise IllegalStreamOperationException("Tying to reduce reducing a stream with no values")

        b = next(struct, self.eol) if initializer is None else initializer
        if b is self.eol and initializer is None:
            return a

        _initial = _function(a,b)
        _curried_function = partial(_function,  *args, **kwargs)
        return reduce(_curried_function, struct, _initial)

    def filter(self, _function, *args, **kwargs):
        _curried_function = partial(_function, *args, **kwargs)
        return self._build(filter(_curried_function, self.structure))

    def tap(self, _function, *args, **kwargs):
        def _tap(function, iterable):
            for x in iterable:
                function(x)
                yield x
        _curried_function = partial(_function, *args, **kwargs)
        return self._build(_tap(_curried_function, self.structure))

    def _take(self, n, iterable):
        for i, val in enumerate(iterable):
            if i == n:
                break
            else:
                yield val

    def take(self, n):
        return self._build(self._take(n, self.structure))


    def _drop(self, n, iterable):
        for i, val in enumerate(iterable):
            if i >= n :
                yield val

    def drop(self, n):
        return self._build(self._drop(n, self.structure))

    def drain(self):
        for _ in self.structure:
            continue

if __name__ == "__main__":
    pass
