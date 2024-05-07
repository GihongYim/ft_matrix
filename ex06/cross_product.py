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
