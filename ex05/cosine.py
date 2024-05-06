import sys
sys.path.append('..')

from ex00.vector import Vector
from ex00.matrix import Matrix


def angle_cos(u: 'Vector', v: 'Vector'):
	return u.dot(v) / (u.norm() * v.norm())

u = Vector([1.0, 0.0])
v = Vector([1.0, 0.0])
print(angle_cos(u, v))

u = Vector([1.0, 0.0])
v = Vector([0.0, 1.0])
print(angle_cos(u, v))

u = Vector([-1.0, 1.0])
v = Vector([1.0, -1.0])
print(angle_cos(u, v))

u = Vector([2.0, 1.0])
v = Vector([4.0, 2.0])
print(angle_cos(u, v))

u = Vector([1.0, 2.0, 3.0])
v = Vector([4.0, 5.0, 6.0])
print(angle_cos(u, v))