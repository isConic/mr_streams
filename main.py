from functools import partial
import pprint

pp = pprint.PrettyPrinter()


class Streams():
    def __init__(self, source = None):
        self.source = source
        self.bound_pipeline = None
        self.str = []

    def map(self, fn, *args, **kwargs):
        self.str.append((map, fn, args, kwargs))
        return self

    def tap(self, fn, *args, **kwargs):
        def _tap(fn, iterable, *args, **kwargs):
            for value in iterable:
                fn(value, *args, **kwargs)
                yield value

        self.str.append((_tap, fn, args, kwargs))
        return self

    def filter(self, fn, *args, **kwargs):
        self.str.append((filter, fn, args, kwargs))
        return self

    def attach(self, data):
        self.str = self.__build(data)

    def __build(self, data):
        structure = iter(data)

        for operation, function, args, kwargs in self.str:
            structure = operation(partial(function,*args, **kwargs), structure)
        return structure

    def __next__(self):
        if self.source != None:
            if self.bound_pipeline == None:
                self.bound_pipeline = self.__build(self.source)
            return next(self.bound_pipeline)
        else:
            return self

    def __iter__(self):
        if self.source != None:
            if self.bound_pipeline == None:
                self.bound_pipeline = self.__build(self.source)
            return self.bound_pipeline

    def __repr__(self):
        return pprint.pformat(self.str)

    def __str__(self):
        return pprint.pformat(self.str)

