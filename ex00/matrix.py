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
    
    @staticmethod
    def identity(n: int) -> 'Matrix':
        try:
            if n <= 0:
                raise ValueError("dim number should be positive integer")
        except Exception as e:
            print(e)
            exit(1)
        id = Matrix([[0.0 for _ in range(n)] for _ in range(n)])
        for i in range(n):
            id[i][i] = 1.0
        return id

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
    
    # def cofactor(self, n: int, m: int) -> float:
    #     try :
    #         if self.dim[0] != self.dim[1]:
    #             raise ValueError("cofactor: matrix is not square")
    #         if self.dim[0] <= 1:
    #             raise ValueError("cofactor: matrix row column length more than 1")
    #     except Exception as e:
    #         print(e)
    #         exit(1)

    #     cof = Matrix.zeros(self.dim[0] - 1, self.dim[1] - 1)
    #     row = 0
    #     n -= 1
    #     m -= 1
    #     for i in range(self.dim[0]):
    #         if i == n: continue
    #         col = 0
    #         for j in range(self.dim[1]):
    #             if j == m: continue
    #             cof.matrix[row][col] = self.matrix[i][j]
    #             col += 1
    #         row += 1
    #     return cof.determinant()

    def determinant(self):
        try :
            if self.dim[0] != self.dim[1]:
                raise ValueError("matrix is not square")
        except Exception as e:
            print(e)
            exit(1)
        det = 1.0
        upper = Matrix(self.matrix)
        for i in range(upper.dim[0]):
            if upper.matrix[i][i] == 0.0:
                for col in range(i + 1, self.dim[0]):
                    if upper.matrix[col][i] != 0.0:
                        break
                upper.matrix[i], upper.matrix[col] = upper.matrix[col], upper.matrix[i]
                det *= -1
            divisor = upper.matrix[i][i]
            if divisor == 0.0: 
                return 0.0
            for row in range(i + 1, upper.dim[0]):
                coeff = upper.matrix[row][i] / divisor
                for col in range(i, upper.dim[1]):
                    upper.matrix[row][col] -= coeff * upper.matrix[i][col]
        for i in range(upper.dim[0]):
            det *= upper.matrix[i][i]
        return det
    
    def inverse(self):
        try:
            if self.dim[0] != self.dim[1]:
                raise ValueError("dim[0] != dim[1]")
            if self.determinant() == 0.0:
                raise ValueError("matrix is singular")
        except Exception as e:
            print(e)
            exit(1)
        left = Matrix(self.matrix)
        right = Matrix.identity(self.dim[0])

        for i in range(left.dim[0]):
            ## if lead element is zero change rows
            if left.matrix[i][i] == 0.0:
                lead_zero_row = i
                for j in range(i + 1, left.dim[0]):
                    if left.matrix[i][j] != 0.0:
                        lead_zero_row = j
                        break
                if lead_zero_row == i:
                    raise ValueError("matrix singular")
                left[i], left[lead_zero_row] = left[lead_zero_row], left[i]
                right[i], right[lead_zero_row] = right[lead_zero_row], right[i]
            ## divide row to make row that have lead zero
            divisor = left.matrix[i][i]
            for j in range(i, left.dim[1]):
                left.matrix[i][j] /= divisor
            for j in range(right.dim[1]):
                right.matrix[i][j] /= divisor
            ## delete lead zero below this row
            for j in range(left.dim[0]):
                if i == j: continue
                coeff = left.matrix[j][i]
                for k in range(i, left.dim[1]):
                    left.matrix[j][k] -= (coeff * left.matrix[i][k])
                for k in range(right.dim[1]):
                    right.matrix[j][k] -= (coeff * right.matrix[i][k])
        return right
    
    def rank(self) -> int:
        cnt = 0
        ref = self.row_echelon()
        
        for row in range(ref.dim[0]):
            for col in range(ref.dim[1]):
                if ref.matrix[row][col] != 0.0:
                    cnt += 1
                    break
        return cnt


