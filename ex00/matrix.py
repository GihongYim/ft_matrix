from ex00.vector import Vector

class Matrix:
    def __init__(self, b: list[list[float]]):
        try:
            if not isinstance(b, list):
                raise TypeError("b is not list")
            if not isinstance(b[0], list):
                raise TypeError("b is not 2-dim matrix")
        except Exception as e:
            print(e)
            exit(1)
        self.matrix = b

        self.row = len(b)
        self.col = len(b[0])
        self.dim = (len(b), len(b[0]))

        for i in range(len(b)):
            if len(b[i]) != self.col:
                raise "each col has different size"
    def __str__(self):
        result = ""
        for i in range(self.col):
            result += str(self.matrix[i])
            # result += "\n"
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

    def mul_vec(self, vec:'Vector'):
        try:
            if not isinstance(vec, Vector):
                raise TypeError("vec is not Vector")
            if (self.dim[1] != vec.dim):
                raise ValueError("matrix column {self.dim[1]} not equsl vector len {vec.dim[0]}}")
        except Exception as e:
            print(e)
            exit(1)
        mul = Vector([0] * self.dim[0])

        for row in range(self.dim[0]):
            for col in range(self.dim[1]):
                mul.vector[row] += self.matrix[row][col] * vec.vector[col]
        
        return mul


    def mul_mat(self, mat:'Matrix'):
        try:
            if not isinstance(mat, Matrix):
                raise TypeError("mat is not Matrix")
            if (self.dim[1] != mat.dim[0]):
                raise ValueError(
                    "left matrix column {self.dim[1]} \
                    not equal right Matrix row {mat.dim[0]}}")
        except Exception as e:
            print(e)
            exit(1)
        mul = Matrix(self.matrix)
        for i in range(self.dim[0]):
            for j in range(mat.dim[1]):
                mul[i][j] = 0
                for k in range(self.dim[1]):
                    mul[i][j] += (self.matrix[i][k] + mat.matrix[k][j])
        return mul

