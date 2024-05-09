import sys
sys.path.append('..')

from ex00.vector import Vector
from ex00.matrix import Matrix

u = Matrix([
    [ 1., -1.],
    [-1., 1.],
])

print(u.determinant())
print()

u = Matrix([
    [2., 0., 0.],
    [0., 2., 0.],
    [0., 0., 2.],
])

print(u.determinant())
print()


u = Matrix([
    [8., 5., -2.],
    [4., 7., 20.],
    [7., 6., 1.],
])

print(u.determinant())
print()

u = Matrix([
    [ 8., 5., -2., 4.],
    [ 4., 2.5, 20., 4.],
    [ 8., 5., 1., 4.],
    [28., -4., 17., 1.],
])

print(u.determinant())
print()