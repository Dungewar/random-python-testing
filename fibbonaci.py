def fibb(n: int):
    if n < 2:
        return n
    else:
        return fibb(n - 1) + fibb(n - 2)


def fibb2(n: int):
    cheese: list[int] = [0, 1]
    while True:
        if len(cheese) > n:
            return cheese[n]
        else:
            cheese.append(cheese[len(cheese) - 2] + cheese[len(cheese) - 1])


for i in range(0, 50):
    print(f"i={i} fibb={fibb2(i)}")
