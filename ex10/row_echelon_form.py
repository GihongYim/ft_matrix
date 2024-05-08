import sys
sys.path.append('..')

from ex00.vector import Vector
from ex00.matrix import Matrix

if __name__ == "__main__":
    u = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.],
    ])
    print(u.row_echelon())


    u = Matrix([
        [1.0, 2.0],
        [3.0, 4.0]
    ])
    print(u.row_echelon())