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