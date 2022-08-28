
from .quaternion import Quaternion, qi, qj, qk

class QuaternionArray:

    def __init__(self, *args, **kwargs):

        match len(args):
            case 0:
                if kwargs and False:
                    pass
                else:
                    self.array = []
            case 1:
                array = args[0]
                if isinstance(array, (tuple, list)):
                    if False not in (isinstance(q, Quaternion) for q in array):
                        self.array = list(array)
                    else:
                        print("ValueError", array)
                        self.array = []
                elif isinstance(array, Quaternion):
                    q = array
                    self.array = [q]
            case _:
                if False not in (isinstance(q, Quaternion) for q in args):
                    self.array = list(args)
                else:
                    print("ValueError")
                    self.array = []

    @property
    def string(self):
        s = f"Quaternion array of length {len(self)}"
        for q in self.array:
            #s += '\n    '+str(tuple((' '*(float(x) >= 0)+f"{x}" for x in q.components))).replace('\'', '')
            s += f'\n    {q}'
        return s

    def __repr__(self):
        return self.string

    def __str__(self):
        return self.string

    def __len__(self):
        return len(self.array)

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[int(index)] = Quaternion(value)

    def __neg__(self):
        return self.__class__(list((-q for q in self.array)))

    def rotate(self, axis, angle):
        for q in self.array:
            q.rotate(axis, angle)
        return self

    def morphed(self, i_prime, j_prime, k_prime):
        return self.__class__(list([q.morphed(i_prime, j_prime, k_prime) for q in self.array]))

    def unmorphed(self, i_prime, j_prime, k_prime):
        return self.__class__(list([q.unmorphed(i_prime, j_prime, k_prime) for q in self.array]))

    def copy(self):
        return self.__class__([q.copy() for q in self.array])

QA = QuaternionArray

# Unit quaternions in an array
UNIT_QUATERNIONS = QA([qi, qj, qk])
# Don't change these either xd
