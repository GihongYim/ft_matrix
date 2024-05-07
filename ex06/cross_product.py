import sys
sys.path.append('..')

from ex00.vector import Vector
from ex00.matrix import Matrix

def cross_product(u: 'Vector', v: 'Vector') -> 'Vector':
    try:
        if not isinstance(u, Vector):
            raise TypeError("u is not vector")
        if not isinstance(v, Vector):
            raise TypeError("v is not vector")
        if u.size != 3:
            raise ValueError("u size is not 3")
        if v.size != 3:
            raise ValueError("v size is not 3")
    except Exception as e:
        print(e)
        exit(1)

    w = Vector([0.0, 0.0, 0.0])

    w.vector[0] = u.vector[1] * v.vector[2] - u.vector[2] * v.vector[1]
    w.vector[1] = -u.vector[0] * v.vector[2] + u.vector[2] * v.vector[0]
    w.vector[2] = u.vector[0] * v.vector[1] - u.vector[1] * v.vector[0]
    return w

if __name__ == "__main__":
    u = Vector([0.0, 0.0, 1.0])
    v = Vector([1.0, 0.0, 0.0])
    print(cross_product(u, v))