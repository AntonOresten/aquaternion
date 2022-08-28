# aquaternion
 
This package includes classes that can be used for calculating 3-dimensional translation and rotation.

## Installation

## How to use

```python
from aquaternion import *

q1 = Quaternion([0, -7, 2, 9])
q2 = Q([4, -1, -5])

print(q1 + q2)
print(q1 * q2)
```

### Output:
```
(0.000 -3.000i +1.000j +4.000k)
(0.000 -3.000i +1.000j +4.000k)
```
