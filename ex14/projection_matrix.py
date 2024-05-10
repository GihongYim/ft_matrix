import sys
sys.path.append('..')

from ex00.vector import Vector
from ex00.matrix import Matrix
import math
def projection(fov: float, ratio: float, near: float, far: float) -> 'Matrix':
    tan_half_fov = math.tan(fov / 2)
    proj_matrix = Matrix.zeros(4, 4)

    proj_matrix.matrix[0][0] = 1.0 / (ratio * tan_half_fov)
    proj_matrix.matrix[1][1] = 1.0 / tan_half_fov
    proj_matrix.matrix[2][2] = -(far + near) / (far - near)
    proj_matrix.matrix[2][3] = 2.0 * far * near / (far - near)
    proj_matrix.matrix[3][2] = -1.0

    return proj_matrix

if __name__ == "__main__":
    fov = math.pi / 2.0
    print(fov)
    ratio = 16/9
    near = 0.01
    far = 10.0
    proj_matrix = projection(fov, ratio, near, far)
    print(proj_matrix)