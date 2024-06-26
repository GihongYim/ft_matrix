import sys
sys.path.append('..')

from ex00.vector import Vector
from ex00.matrix import Matrix


u = Matrix([
    [1., 0., 0.],
    [0., 1., 0.],
    [0., 0., 1.],
])

print(u.rank())


u = Matrix([
    [ 1., 2., 0., 0.],
    [ 2., 4., 0., 0.],
    [-1., 2., 1., 1.],
])

print(u.rank())


u = Matrix([
    [ 8., 5., -2.],
    [ 4., 7., 20.],
    [ 7., 6., 1.],
    [21., 18., 7.],
])

print(u.rank())