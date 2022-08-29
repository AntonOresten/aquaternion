
from time import perf_counter

def run_test(function, args=(), n=10000):
    start = perf_counter()
    for _ in range(n):
        function(*args)
    end = perf_counter()
    print(f"Ran function '{function.__name__}' {n} times in {end-start:.9f} seconds (avg: {(end-start)/n:.9f}s)")


from aquaternion import *

q1, q2 = Q([1,2,3]), Q([-1, 5, 100, -3])

run_test(Q.__add__, (q1, q2))
run_test(Q.__radd__, (q1, q2))
run_test(Q.__neg__, (q1,))
run_test(Q.__sub__, (q1, q2))
run_test(Q.__rsub__, (q1, q2))
run_test(Q.__mul__, (q1, q2))
run_test(Q.__rmul__, (q1, q2))
run_test(Q.__truediv__, (q1, q2))
run_test(Q.__rtruediv__, (q1, q2))


# norm = lambda vector: sum([x**2 for x in vector])**0.5
# run_test(np.linalg.norm, ([1, 2, 3],))
# run_test(norm, ([1, 2, 3],))
