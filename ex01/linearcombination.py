import sys
sys.path.append('..')

from ex00.vector import Vector
from ex00.matrix import Matrix

def linear_combination(v:list['Vector'], coefs:list[float]):
    if len(v) != len(coefs):
        raise "v, coefs have not equal size"
    result = Vector([0] * v[0].size)
    for i in range(len(v)):
        v[i].scl(coefs[i])
    for i in range(len(v)):
        result.add(v[i])

    return result


if __name__ == "__main__":
    e1 = Vector([1.0, 0.0, 0.0])
    e2 = Vector([0.0, 1.0, 0.0])
    e3 = Vector([0.0, 0.0, 1.0])

    v1 = Vector([1.0, 2.0, 3.0])
    v2 = Vector([0.0, 10.0, -100.0])

    print(linear_combination([e1, e2, e3], [10.0, -2.0, 0.5]))
    print(linear_combination([v1, v2], [10.0, -2.0]))


