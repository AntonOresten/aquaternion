
from .quaternion import *
from .array import *

class UnitVectors:
    """
    Somewhat analogous to a 3x3 matrix
    """

    def __init__(self, unit_vectors):
        if len(list(unit_vectors)) != 3:
            raise IndexError("Need three unit vectors")
        if False in (isinstance(q, Quaternion) for q in list(unit_vectors)):
            raise TypeError("All elements must be Quaternions")
        
        self.unit_vectors = list(unit_vectors)

    @property
    def i(self):
        return self.unit_vectors[0]

    @property
    def j(self):
        return self.unit_vectors[1]

    @property
    def k(self):
        return self.unit_vectors[2]


    def __str__(self):
        return "Unit Quaternion Vectors" + ''.join(map(lambda q: '\n'+f'    {q}', self.unit_vectors))


    def __repr__(self):
        return f"{self.__class__.__name__}([{', '.join(map(lambda q: repr(q), self.unit_vectors))}])"


    def __len__(self):
        return 3


    def __getitem__(self, index):
        return self.unit_vectors[index]


    def __setitem__(self, index, value):
        self.unit_vectors[index] = Quaternion(value)


    def copy(self):
        return self.__class__([q.copy() for q in self.unit_vectors])


    def __neg__(self):
        return self.__class__([-q for q in self.unit_vectors])


    def rotated(self, axis, angle):
        return self.__class__([q.rotated(axis, angle) for q in self.unit_vectors])

    def rotate(self, axis, angle):
        [q.rotate(axis, angle) for q in self.unit_vectors]
        return self


    def morphed(self, i_prime, j_prime, k_prime):
        return self.__class__([q.morphed(i_prime, j_prime, k_prime) for q in self.unit_vectors])

    def morph(self, i_prime, j_prime, k_prime):
        [q.morph(i_prime, j_prime, k_prime) for q in self.unit_vectors]
        return self


    def unmorphed(self, i_prime, j_prime, k_prime):
        inverse_determinant = float(i_prime.x*(j_prime.y*k_prime.z-k_prime.y*j_prime.z) - j_prime.x*(i_prime.y*k_prime.z-k_prime.y*i_prime.z) + k_prime.x*(i_prime.y*j_prime.z-j_prime.y*i_prime.z))
        q1 = inverse_determinant*Q([(j_prime.y*k_prime.z-k_prime.y*j_prime.z), -(i_prime.y*k_prime.z-k_prime.y*i_prime.z), (i_prime.y*j_prime.z-j_prime.y*i_prime.z)])
        q2 = inverse_determinant*Q([-(j_prime.x*k_prime.z-k_prime.x*j_prime.z), (i_prime.x*k_prime.z-k_prime.x*i_prime.z), -(i_prime.x*j_prime.z-j_prime.x*i_prime.z)])
        q3 = inverse_determinant*Q([(j_prime.x*k_prime.y-k_prime.x*j_prime.y), -(i_prime.x*k_prime.y-k_prime.x*i_prime.y), (i_prime.x*j_prime.y-j_prime.x*i_prime.y)])
        return self.morphed(q1, q2, q3)

    def unmorph(self, i_prime, j_prime, k_prime):
        self.unit_vectors = self.unmorphed(i_prime, j_prime, k_prime).unit_vectors
        return self


UV = UnitVectors([q.copy() for q in [qi, qj, qk]])