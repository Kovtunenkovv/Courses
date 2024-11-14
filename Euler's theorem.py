import time
from numba import njit #Numba can be used to optimize CPU and GPU

@njit(fastmath=True, parallel=True)
def main_numba():
    for a in range(1, 151):
        for b in range(a, 151):
            for c in range(b, 151):
                for d in range(c, 151):
                    for e in range(d, 151):
                        if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                            print(f'a = {a}, b = {b}, c = {c}, d = {d}, e = {e}')
                            return (a + b + c + d + e)
                            
    return None

time1 = time.time()
result_numba = main_numba()
time2 = time.time()

print(f'Numba Execution Time: {round(time2 - time1)} second')
print(f'Result: {result_numba}')

"""____________________________________________
a = 27, b = 84, c = 110, d = 133, e = 144
Numba Execution Time: 1 second
Result: 498
____________________________________________"""
