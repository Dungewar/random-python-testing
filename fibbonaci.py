import sys
import time
from pickletools import long4


def fibb(n: int) -> int:
    if n < 2:
        return n
    else:
        return fibb(n - 1) + fibb(n - 2)


def fibb2(n: int) -> int:
    fibb_numbers: list[int] = [0, 1]
    while True:
        if len(fibb_numbers) > n:
            return fibb_numbers[n]
        else:
            fibb_numbers.append(fibb_numbers[len(fibb_numbers) - 2] + fibb_numbers[len(fibb_numbers) - 1])


def fibb3(n: int) -> int:
    a, b, c = 0, 1, 0
    while c < n:
        a, b, c = a + b, a, c + 1
    return a


print(flush=False)
# for i in range(0, 10000):

start = int(round(time.time() * 1000))
i = 1000000
sys.set_int_max_str_digits(2000000)
print(f"i={i} fibb={fibb3(i)}")
end = int(round(time.time() * 1000))
print(f'Time taken: {end - start}ms')
