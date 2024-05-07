import sys
sys.path.append('..')

from ex00.vector import Vector
from ex00.matrix import Matrix

u = Vector([0.0, 0.0])
v = Vector([1.0, 1.0])
print(u.dot(v))


u = Vector([1.0, 1.0])
v = Vector([1.0, 1.0])
print(u.dot(v))


u = Vector([-1.0, 6.0])
v = Vector([3.0,.0])
print(u.dot(v))