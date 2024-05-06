import sys
sys.path.append('..')

from ex00.vector import Vector
from ex00.matrix import Matrix

u = Vector([0.0, 0.0, 0.0])
print(u.norm_1(), u.norm(), u.norm_inf())

u = Vector([1.0, 2.0, 3.0])
print(u.norm_1(), u.norm(), u.norm_inf())

u = Vector([-1.0, -2.0])
print(u.norm_1(), u.norm(), u.norm_inf())
