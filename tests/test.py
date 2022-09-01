
# TODO: make proper tests

from time import perf_counter

def run_test(function, args=(), n=10000):
    start = perf_counter()
    for _ in range(n):
        function(*args)
    end = perf_counter()
    print(f"Ran function '{function.__name__}' {n} times in {end-start:.9f} seconds (avg: {(end-start)/n:.9f}s)")


# q1, q2 = Q([1,2,3]), Q([-1, 5, 100, -3])

# run_test(Q.__add__, (q1, q2))
# run_test(Q.__radd__, (q1, q2))
# run_test(Q.__neg__, (q1,))
# run_test(Q.__sub__, (q1, q2))
# run_test(Q.__rsub__, (q1, q2))
# run_test(Q.__mul__, (q1, q2))
# run_test(Q.__mul__, (q1, 1))
# run_test(Q.__rmul__, (q1, q2))
# run_test(Q.__rmul__, (q1, 1))
# run_test(Q.__truediv__, (q1, q2))
# run_test(Q.__rtruediv__, (q1, q2))

from aquaternion import *

def tests():
    assert repr(Q([0., 1, 2, 3])) == "Q([0.0, 1, 2, 3])"
    assert str(Q([0., 1, 2, 3])) == "(0.000 +1.000i +2.000j +3.000k)"
    
    assert qi.w == 0
    assert qi.x == 1
    assert qj.y == 1
    assert qk.z == 1
    
    assert Q([1, 2, 2]).norm == 3
    assert abs(3*qi - 4*qj) == 5
    assert (2*qi).normalized == qi
    assert Q([2, 0, 4, 8]).conjugate == Q([2, -0, -4, -8])
    assert Q([0, 3, 4]).sum_of_squares == 25
    assert (2 * qi).inverse == -0.5 * qi
    
    assert Q([1, 2, 3]) + Q([-1, 2, -1]) == Q([0, 4, 2])
    assert Q([4, 3, 2]) + 5 == Q([5, 4, 3, 2])
    assert Q([7, 2, 3]) - Q([4, -6, -4]) == Q([3, 8, 7])
    assert Q([7, 2, 3]) - 2. == Q([-2, 7, 2, 3])
    assert 3. - Q([1, 4, 1]) == Q([3, -1, -4, -1])
    assert qi * qj == qk
    assert (2 * qi) * (qj * 0.5) == Q([0, 0, 1])
    assert qk / qj == Q([1, 0, 0])
    assert qi / 5 == Q([0.2, 0, 0])
    assert 5 / qi == Q([-5, 0, 0])
    
    assert round(Q([pi, 3.125, 3]), 2) == Q([3.14, 3.12, 3])
    assert bool(qi) is True
    assert bool(Q([0, 0, 0])) is False
    assert (qi == qj*qk) is True
    assert (qi*qk != qj) is True
    assert len(qi) == 4
    
    assert Q([1, 2, 3, 4])[2] == 3
    assert Q([8, 6, 4, 0]).components == [8, 6, 4, 0]
    assert Q([2., 7, 1, 8]).copy() == Q([2., 7, 1, 8])
    assert qi.vector3 == [1, 0, 0]
    assert (1 + qi + qj).qvector3 == qi + qj
    
    assert qi.rotated(qk, pi/2) == qj
    assert qi.morphed(2*qk, 3*qj, 4*qi) == 2*qk
    assert (2*qk).unmorphed(2*qk, 3*qj, 4*qi) == qi

    assert Q.dot(Q([1, 2, 3]), Q([1, 2, 3, 4])) == (Q([1, 2, 3])*Q([1, 2, 3, 4])).w.__neg__()

if __name__ == '__main__':
    tests()


# norm = lambda vector: sum([x**2 for x in vector])**0.5
# run_test(np.linalg.norm, ([1, 2, 3],))
# run_test(norm, ([1, 2, 3],))
