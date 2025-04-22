def fibb(n: int):
    if n < 2:
        return n
    else:
        return fibb(n-1) + fibb(n-2)

print(fibb(50))