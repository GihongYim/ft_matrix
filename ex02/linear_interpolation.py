import sys
sys.path.append('..')

from ex00.vector import Vector
from ex00.matrix import Matrix

def lerp(u: float, v: float, t: float):
    try:
        if t < 0 or t > 1:
            raise ValueError("t should be in [0.0, 1.0]")
        if type(u) != type(v):
            raise TypeError("type of u and v not equal")
        if isinstance(u, float):
            return (1 - t) * u + t * v
        elif isinstance(u, Vector) or isinstance(v, Matrix):
            u.scl(1 - t)
            v.scl(t)
            u.add(v)
            return u
    except Exception as e:
        print(e)
        exit(1)

if __name__ == "__main__":
    print(lerp(0.0, 1.0, 0.0))
    print(lerp(0.0, 1.0, 1.0))
    print(lerp(0.0, 1.0, 0.5))
    print(lerp(21.0, 42.0, 0.3))
    print(lerp(Vector([2.0, 1.0]), Vector([4.0, 2.0]), 0.3))
    print(lerp(Matrix([[2.0, 1.0], [3.0, 4.0]]),
                Matrix([[20.0, 10.0], [30.0, 40.0]]), 0.5))

    