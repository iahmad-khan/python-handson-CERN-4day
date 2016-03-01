from itertools import izip, count

# Using itertools
def ienumerate(data, start=0):
    return izip(count(start), data)

# Using a generator function
def genumerate(data, count=0):
    for datum in data:
        yield count, datum
        count += 1

# Using an ad-hoc class
class cenumerate:

    def __init__(self, data, start=0):
        self._iterator = iter(data)
        self._count = start

    def next(self):
        self._count += 1
        return (self._count-1, self._iterator.next())

    def __iter__(self):
        return self

