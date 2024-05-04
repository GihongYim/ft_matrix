class Matrix:
    def __init__(self, b: list[list[float]]):
        self.matrix = b
        # if isinstance(b, list):
        #     raise "b is not list"
        # if isinstance(b[0], list):
        #     raise "b is not 2-dim matrix"
        self.row = len(b)
        self.col = len(b[0])

        for i in range(len(b)):
            if len(b[i]) != self.col:
                raise "each col has different size"
    def __str__(self):
        result = ""
        for i in range(self.col):
            result += str(self.matrix[i])
            result += "\n"
        return str(result)
        

    def add(self, v):
        if self.row != v.row or self.col != v.row:
            raise "matrix size are not equal"
        
        for i in range(self.row):
            for j in range(self.col):
                self.matrix[i][j] += v.matrix[i][j]

    def sub(self, v):
        if self.row != v.row or self.col != v.row:
            raise "matrix size are not equal"
        
        for i in range(self.row):
            for j in range(self.col):
                self.matrix[i][j] -= v.matrix[i][j]

    def scl(self, a: float):
        for i in range(self.row):
            for j in range(self.col):
                self.matrix[i][j] *= a
