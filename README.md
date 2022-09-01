# aquaternion
 
This package includes classes that can be used for calculating 3-dimensional translation and rotation.

## Installation

Clone this repository and run the following command:
```
python setup.py install
```

## How to use

### Creating a quaternion:
```python
from aquaternion import *

Q([0, 1, 2, 3])
# The four numbers correspond to the w, x, y, and z components respectively.

# Creating a quaternion with only three numbers will assign the values to the x, y, and z (imaginary) components,
# and leave w with the default value of 0
Q([1, 2, 3])
```

### Performing arithmetics:
```python
q1 = Q([-7, 2, 9])
q2 = Q([4, -1, -5])

print(q1 + q2)
print(q1 * q2)
print(Q([0, 3, 4]).norm)
```

Output:
```
(0.000 -3.000i +1.000j +4.000k)
(75.000 -1.000i +1.000j -1.000k)
5.0
```

## Linear Algebra
The *morphed* method is equivalent to replacing the unit vectors of a Quaternion.
The *unmorphed* method is the inverse of *morphed*. Thus:
```python
q = Q([1, 2, 3])

# This coordinate system is rotated tau/3 radians around the Q([1, 1, 1]) axis, compared to normal.
new_unit_vectors = UnitVectors([qj, qk, qi])

# This will be equal to Q([3, 1, 2])
q_prime = q.morphed(*new_unit_vectors)

# This will create an unmorphed q_prime, and will be equal to q, Q([1, 2, 3])
original_q = q_prime.unmorphed(*new_unit_vectors)
```
*morph/unmorph/rotate/normalize* will change an instance whereas *morphed/unmorphed/rotated/normalized* will create a new one.
