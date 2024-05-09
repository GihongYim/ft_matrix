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
        self.dim = (len(b), len(b[0]))

        for i in range(len(b)):
            if len(b[i]) != self.dim[1]:
                raise "each col has different size"

    def __getitem__(self, index):
        try:
            if index >= self.dim[0]:
                raise IndexError("row index more than matrix row length")
            return self.matrix[index]
        except Exception as e:
            print(e)
            exit(1)

    @staticmethod
    def zeros(n: int, m: int) -> 'Matrix':
        try:
            if n <= 0 or m <= 0:
                raise ValueError("dim number should be positive integer")
        except Exception as e:
            print(e)
            exit(1)
        return Matrix([[0.0 for _ in range(m)] for _ in range(n)])
        

    def __str__(self):
        result = ""
        for i in range(self.dim[0]):
            result += str(self.matrix[i])
            if i != self.dim[0] - 1:
                result += "\n"
        return str(result)
        

    def add(self, v):
        if self.row != v.row or self.col != v.row:
            raise "matrix size are not equal"
        
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                self.matrix[i][j] += v.matrix[i][j]

    def sub(self, v):
        if self.row != v.row or self.col != v.row:
            raise "matrix size are not equal"
        
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                self.matrix[i][j] -= v.matrix[i][j]

    def scl(self, a: float):
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
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


    def mul_mat(self, mat:'Matrix') -> 'Matrix':
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
        mul = Matrix([[0.0] * mat.dim[1] for _ in range(self.dim[0])])
        for i in range(self.dim[0]):
            for j in range(mat.dim[1]):
                for k in range(self.dim[1]):
                    mul.matrix[i][j] += (self.matrix[i][k] * mat.matrix[k][j])
        return mul
    
    def trace(self) -> int:
        try:
            if self.dim[0] != self.dim[1]:
                raise ValueError("trace : matrix is not square matrix")
        except Exception as e:
            print(e)
            exit(1)

        result = 0.0
        for i in range(self.dim[0]):
            result += self.matrix[i][i]
        return result
    
    def transpose(self) -> 'Matrix':
        tr = Matrix.zeros(self.dim[1], self.dim[0])
        for row in range(self.dim[0]):
            for col in range(self.dim[1]):
                tr.matrix[col][row] = self.matrix[row][col]
        return tr

    def row_echelon(self) -> 'Matrix':
        ref = Matrix(self.matrix)
        for row in range(ref.dim[0]):
            col = 0
            while (col < ref.dim[1]):
                if ref.matrix[row][col] != 0.0:
                    break
                col += 1
            if col == ref.dim[1]:
                continue
            divisor = ref.matrix[row][col]
            if divisor != 1.0:
                for i in range(col, ref.dim[1]):
                    ref.matrix[row][i] /= divisor
            for i in range(ref.dim[0]):
                if i == row : continue
                if ref.matrix[i][col] == 0.0: continue
                divisor = ref.matrix[i][col]
                for j in range(col, ref.dim[1]):
                    ref.matrix[i][j] -= ref.matrix[row][j] * divisor
        return ref

    def determinant(self):
        try :
            if self.dim[0] != self.dim[1]:
                raise ValueError("matrix is not square")
        except Exception as e:
            print(e)
            exit(1)
        ref = self.row_echelon()
        det = 1.0
        for i in range(ref.dim[0]):
            det *= ref.matrix[i][i]
        return det

        