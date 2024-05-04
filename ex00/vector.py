class Vector:
    def __init__(self, v: list[float]):
        self.v = v
        self.size = len(v)

    def __str__(self):
        return str(self.v)
            

    def add(self, v: 'Vector') -> None:
        if self.size != v.size:
            raise "two vector size not equal"
        for i in range(self.size):
            self.v[i] += v.v[i]

    def sub(self, v: 'Vector') -> None:
        if self.size != v.size:
            raise "two vector size not equal"
        for i in range(self.size):
            self.v[i] -= v.v[i]

    def scl(self, a: 'int') -> None:
        if not isinstance(a, float):
            raise TypeError
        for i in range(self.size):
            self.v[i] *= a
