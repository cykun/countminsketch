import hashlib
import array


class CountMinSketch(object):
    # m is the size of hash tables, larger implies smaller overesttimation.
    # d is the amount of hash table, larger implies lower probability of overestimation.
    def __init__(self, m, d) -> None:
        if not m or not d:
            raise ValueError("")
        self.m = m
        self.d = d
        self.n = 0
        self.tables = []
        for _ in range(d):
            table = array.array('L', (0 for _ in range(m)))
            self.tables.append(table)

    def __hash(self, x) -> int:
        md5 = hashlib.md5(str(hash(x)).encode("utf8"))
        for i in range(self.d):
            md5.update(str(i).encode("utf8"))
            yield int(md5.hexdigest(), 16) % self.m

    def add(self, x, value=1):
        self.n += value
        for table, i in zip(self.tables, self.__hash(x)):
            table[i] += value

    def query(self, x):
        return min(table[i] for table, i in zip(self.tables, self.__hash(x)))

    def __getitem__(self, x):
        return self.query(x)

    def __len__(self):
        return self.n
