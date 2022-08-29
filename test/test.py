
from aquaternion import *

from time import perf_counter

n = 10000

q1, q2 = Q([1,2,3]), Q([-1, 5, 100, -3])

start = perf_counter()
for q in range(n):
    q1+q2
end = perf_counter()
print(f"Finished {n} quaternion addition in {end-start} seconds ({(end-start)/n:.6f}) sec")

start = perf_counter()
for q in range(n):
    q1*q2
end = perf_counter()
print(f"Finished {n} quaternion multiplications in {end-start} seconds ({(end-start)/n:.6f}) sec")

start = perf_counter()
for q in range(n):
    q1/q2
end = perf_counter()
print(f"Finished {n} quaternion division in {end-start} seconds ({(end-start)/n:.6f}) sec")

start = perf_counter()
for q in range(n):
    q1.morphed(q2, q2+qj, q2+qk)
end = perf_counter()
print(f"Finished {n} quaternion morphing in {end-start} seconds ({(end-start)/n:.6f}) sec")