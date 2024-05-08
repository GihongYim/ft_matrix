import sys
sys.path.append('..')

from ex00.vector import Vector
from ex00.matrix import Matrix

if __name__ == "__main__":
    u = Matrix([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0]
    ])
    print(u)
    print(u.transpose())