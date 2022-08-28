# aquaternion
 
This package includes classes that can be used for calculating 3-dimensional translation and rotation.

## Installation

## How to use

### Creating a quaternion:
```python
# The same quaternion can be created in different ways:
Q(0, 1, 2, 3)
Q([0, 1, 2, 3])
# The four numbers correspond to the w, x, y, z components respectively.

# The w component is 0 by default.
# Creating a quaternion with only three numbers will assign the values to the x, y, z (imaginary) components.
Q(1, 2, 3)
Q([1, 2, 3])
```

### Performing arithmetic:
```python
from aquaternion import *

q1 = Q([0, -7, 2, 9])
q2 = Q([4, -1, -5])

print(q1 + q2)
print(q1 * q2)
```

### Output:
```
(0.000 -3.000i +1.000j +4.000k)
(0.000 -3.000i +1.000j +4.000k)
```
