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
    print()

    u = Matrix([
        [1.0, 2.0],
        [3.0, 4.0]
    ])
    print(u.row_echelon())
    print()
    u = Matrix([
        [1., 2.],
        [2., 4.],
    ])
    print(u.row_echelon())
    print()

    u = Matrix([
        [8., 5., -2., 4., 28.],
        [4., 2.5, 20., 4., -4.],
        [8., 5., 1., 4., 17.],
    ])
    print(u.row_echelon())
    print()
