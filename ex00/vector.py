class Vector:
    def __init__(self, v: list[float]):
        self.vector = v
        self.size = len(v)

    def __str__(self):
        result = ""
        for i in range(self.size):
            result += "[" + str(self.vector[i]) + "]\n"
        return result
            

    def add(self, v: 'Vector') -> None:
        if self.size != v.size:
            raise "two vector size not equal"
        for i in range(self.size):
            self.vector[i] += v.vector[i]

    def sub(self, v: 'Vector') -> None:
        if self.size != v.size:
            raise "two vector size not equal"
        for i in range(self.size):
            self.vector[i] -= v.vector[i]

    def scl(self, a: 'int') -> None:
        if not isinstance(a, float):
            raise TypeError
        for i in range(self.size):
            self.vector[i] *= a
    
    def dot(self, v : 'Vector'):
        if self.size != v.size:
            raise ValueError("dot produce : vectors size not equal")
        
        value = 0.0
        for i in range(v.size):
            value += (self.vector[i] * v.vector[i])
        return value
    
    def norm_1(self):
        norm = 0.0
        for i in range(self.size):
            norm += abs(self.vector[i])
        return norm
    
    def norm(self):
        norm = 0.0
        for i in range(self.size):
            norm += self.vector[i] ** 2
        return norm ** (0.5)
    
    def norm_inf(self):
        norm = 0.0
        for i in range(self.size):
            if abs(self.vector[i]) > norm:
                norm = abs(self.vector[i])
        return norm

        